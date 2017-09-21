# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# CHNetworkSegment datasource
# ----------------------------------------------------------------------
# Copyright (C) 2007-2017 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
from __future__ import absolute_import
# NOC modules
from .base import BaseDataSource
from noc.inv.models.networksegment import NetworkSegment


class CHAdministrativeDomainDataSource(BaseDataSource):
    name = "ch_networksegment"

    def extract(self):
        r = []
        for ns in NetworkSegment.objects.all().order_by("id"):
            r += [(
                ns.get_bi_id(),
                ns.id,
                ns.name,
                ns.parent.get_bi_id() if ns.parent else ""
            )]
        return r