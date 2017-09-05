# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Network Segment
# ---------------------------------------------------------------------
# Copyright (C) 2007-2017 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
from __future__ import absolute_import
import operator
import cachetools
from threading import Lock
# Third-party modules
from mongoengine.document import Document
from mongoengine.fields import (StringField, DictField, ReferenceField,
                                ListField, BooleanField, IntField,
                                EmbeddedDocumentField, LongField)
from django.db.models.aggregates import Count
# NOC modules
from noc.lib.nosql import ForeignKeyField
from noc.sa.models.managedobjectselector import ManagedObjectSelector
from noc.main.models.remotesystem import RemoteSystem
from noc.sa.models.servicesummary import ServiceSummary, SummaryItem, ObjectSummaryItem
from noc.core.model.decorator import on_delete_check
from noc.core.defer import call_later
from noc.core.bi.decorator import bi_sync
from .networksegmentprofile import NetworkSegmentProfile

id_lock = Lock()


@bi_sync
@on_delete_check(check=[
    ("sa.ManagedObject", "segment"),
    ("inv.NetworkSegment", "parent")
])
class NetworkSegment(Document):
    meta = {
        "collection": "noc.networksegments",
        "strict": False,
        "indexes": ["parent", "sibling", "adm_domains"]
    }

    name = StringField(unique=True)
    parent = ReferenceField("self", required=False)
    profile = ReferenceField(NetworkSegmentProfile, required=True)
    description = StringField(required=False)
    # Management VLAN processing order
    # * d - disable management vlan
    # * e - enable management vlan and get from management_vlan field
    # * p - use profile settings
    management_vlan_policy = StringField(
        choices=[
            ("d", "Disable"),
            ("p", "Profile"),
            ("e", "Enable")
        ],
        default="p"
    )
    management_vlan = IntField(required=False, min_value=1, max_value=4095)
    # MVR VLAN processing order
    # * d - disable multicast vlan
    # * e - enable multicast vlan and get from multicast_vlan field
    # * p - use profile settings
    multicast_vlan_policy = StringField(
        choices=[
            ("d", "Disable"),
            ("p", "Profile"),
            ("e", "Enable")
        ],
        default="p"
    )
    multicast_vlan = IntField(required=False, min_value=1, max_value=4095)

    settings = DictField(default=lambda: {}.copy())
    tags = ListField(StringField())
    # Selectors for fake segments
    # Transition only, should not be used
    selector = ForeignKeyField(ManagedObjectSelector)
    # Sibling segment, if part of larger structure with
    # horizontal links
    sibling = ReferenceField("self")
    # True if segment has alternative paths
    is_redundant = BooleanField(default=False)
    # True if segment is redundant and redundancy
    # currently broken
    lost_redundancy = BooleanField(default=False)
    # Administrative domains which have access to segment
    # Sum of all administrative domains
    adm_domains = ListField(IntField())
    # Collapse object's downlinks on network map
    # when count is above the threshold
    max_shown_downlinks = IntField(default=1000)
    # Objects, services and subscribers belonging to segment directly
    direct_objects = ListField(EmbeddedDocumentField(ObjectSummaryItem))
    direct_services = ListField(EmbeddedDocumentField(SummaryItem))
    direct_subscribers = ListField(EmbeddedDocumentField(SummaryItem))
    # Objects, services and subscribers belonging to all nested segments
    total_objects = ListField(EmbeddedDocumentField(ObjectSummaryItem))
    total_services = ListField(EmbeddedDocumentField(SummaryItem))
    total_subscribers = ListField(EmbeddedDocumentField(SummaryItem))
    # Integration with external NRI and TT systems
    # Reference to remote system object has been imported from
    remote_system = ReferenceField(RemoteSystem)
    # Object id in remote system
    remote_id = StringField()
    # Object id in BI
    bi_id = LongField()

    _id_cache = cachetools.TTLCache(maxsize=100, ttl=60)
    _path_cache = cachetools.TTLCache(maxsize=100, ttl=60)

    def __unicode__(self):
        return self.name

    @classmethod
    @cachetools.cachedmethod(operator.attrgetter("_id_cache"), lock=lambda _: id_lock)
    def get_by_id(cls, id):
        return NetworkSegment.objects.filter(id=id).first()

    @cachetools.cachedmethod(operator.attrgetter("_path_cache"), lock=lambda _: id_lock)
    def get_path(self):
        """
        Returns list of parent segment ids
        :return:
        """
        if self.parent:
            return self.parent.get_path() + [self.id]
        else:
            return [self.id]

    @property
    def effective_settings(self):
        """
        Returns dict with effective settings
        """
        if hasattr(self, "_es"):
            return self._es
        # Build full parent stack
        sstack = [self.settings or {}]
        p = self.parent
        while p:
            sstack = [p.settings or {}] + sstack
            p = p.parent
        # Get effective settings
        es = {}
        for s in sstack:
            for k in s:
                v = s[k]
                if v:
                    # Override parent settings
                    es[k] = v
                elif k in es:
                    # Ignore parent settings
                    del es[k]
        self._es = es
        return es

    @property
    def has_loop(self):
        """
        Check if object creates loop
        """
        if not self.id:
            return False
        p = self.parent
        while p:
            if p.id == self.id:
                return True
            p = p.parent
        return False

    @property
    def managed_objects(self):
        from noc.sa.models.managedobject import ManagedObject

        if self.selector:
            return self.selector.managed_objects
        else:
            siblings = self.get_siblings()
            if len(siblings) == 1:
                q = {"segment": str(siblings.pop().id)}
            else:
                q = {"segment__in": [str(s.id) for s in siblings]}
            return ManagedObject.objects.filter(**q)

    def get_siblings(self, seen=None):
        seen = seen or set()
        ss = set([self])
        seen |= ss
        if self.sibling and self.sibling not in seen:
            ss |= self.sibling.get_siblings(seen)
        seen |= ss
        for s in NetworkSegment.objects.filter(sibling=self):
            ss |= s.get_siblings(seen)
        return ss

    def run_discovery(self):
        """
        Run discovery on whole segment
        """
        for o in self.managed_objects:
            if o.is_managed:
                o.run_discovery()

    @property
    def has_children(self):
        return bool(
            NetworkSegment.objects.filter(
                parent=self.id).only("id").first()
        )

    def set_redundancy(self, status):
        """
        Change interface redundancy status
        :param status:
        :return:
        """
        siblings = list(self.get_siblings())
        filter = {
            "status": {"$ne": status}
        }
        if len(siblings) == 1:
            filter["_id"] = self.id
        else:
            filter["_id"] = {
                "$in": [s.id for s in siblings]
            }

        set_op = {
            "is_redundant": status
        }
        if not status:
            set_op["lost_redundancy"] = False
        NetworkSegment._get_collection().update(
            filter, {
                "$set": set_op
            },
            multi=True
        )

    def set_lost_redundancy(self, status):
        NetworkSegment._get_collection().update({
            "_id": self.id
        }, {
            "$set": {
                "lost_redundancy": bool(status)
            }
        })

    def update_summary(self):
        """
        Update summaries
        :return:
        """
        def update_dict(d1, d2):
            for k in d2:
                if k in d1:
                    d1[k] += d2[k]
                else:
                    d1[k] = d2[k]

        services = {}
        subscribers = {}
        objects = dict(
            (d["object_profile"], d["count"])
            for d in self.managed_objects.values(
                "object_profile"
            ).annotate(
                count=Count("id")
            ).order_by("count"))
        # Direct services
        mo_ids = self.managed_objects.values_list("id", flat=True)
        for ss in ServiceSummary.objects.filter(managed_object__in=mo_ids):
            update_dict(services, SummaryItem.items_to_dict(ss.service))
            update_dict(subscribers, SummaryItem.items_to_dict(ss.subscriber))
        self.direct_services = SummaryItem.dict_to_items(services)
        self.direct_subscribers = SummaryItem.dict_to_items(subscribers)
        self.direct_objects = ObjectSummaryItem.dict_to_items(objects)
        siblings = set()
        for ns in NetworkSegment.objects.filter(parent=self.id):
            if ns.id in siblings:
                continue
            update_dict(services, SummaryItem.items_to_dict(ns.total_services))
            update_dict(subscribers, SummaryItem.items_to_dict(ns.total_subscribers))
            update_dict(objects, ObjectSummaryItem.items_to_dict(ns.total_objects))
            siblings.add(ns.id)
            if ns.sibling:
                siblings.add(ns.sibling.id)
        self.total_services = SummaryItem.dict_to_items(services)
        self.total_subscribers = SummaryItem.dict_to_items(subscribers)
        self.total_objects = ObjectSummaryItem.dict_to_items(objects)
        self.save()
        # Update upwards
        ns = self.parent
        while ns:
            services = SummaryItem.items_to_dict(ns.direct_services)
            subscribers = SummaryItem.items_to_dict(ns.direct_subscribers)
            objects = ObjectSummaryItem.items_to_dict(ns.direct_objects)
            for nsc in NetworkSegment.objects.filter(parent=ns.id):
                update_dict(services, SummaryItem.items_to_dict(nsc.total_services))
                update_dict(subscribers, SummaryItem.items_to_dict(nsc.total_subscribers))
                update_dict(objects, ObjectSummaryItem.items_to_dict(nsc.total_objects))
            ns.total_services = SummaryItem.dict_to_items(services)
            ns.total_subscribers = SummaryItem.dict_to_items(subscribers)
            ns.total_objects = ObjectSummaryItem.dict_to_items(objects)
            ns.save()
            ns = ns.parent

    def update_access(self):
        from noc.sa.models.administrativedomain import AdministrativeDomain
        # Get all own administrative domains
        adm_domains = set(
            d["administrative_domain"]
            for d in self.managed_objects.values(
                "administrative_domain"
            ).annotate(
                count=Count("id")
            ).order_by("count")
        )
        p = set()
        for a in adm_domains:
            a = AdministrativeDomain.get_by_id(a)
            p |= set(a.get_path())
        adm_domains |= p
        # Merge with children's administrative domains
        for s in NetworkSegment.objects.filter(parent=self.id).only("adm_domains"):
            adm_domains |= set(s.adm_domains or [])
        # Check for changes
        if set(self.adm_domains) != adm_domains:
            self.adm_domains = sorted(adm_domains)
            self.save()
            # Propagate to parents
            if self.parent:
                self.parent.update_access()

    def update_uplinks(self):
        call_later(
            "noc.core.topology.segment.update_uplinks",
            60,
            segment_id=self.id
        )
