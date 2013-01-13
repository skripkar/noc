# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## inv.map application
##----------------------------------------------------------------------
## Copyright (C) 2007-2013 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
from collections import defaultdict
## NOC modules
from noc.lib.app import ExtApplication, view
from noc.inv.models.networkchart import NetworkChart
from noc.inv.models.interface import Interface
from noc.inv.models.link import Link
from noc.lib.serialize import json_decode


class MapAppplication(ExtApplication):
    """
    inv.net application
    """
    title = "Network Map"
    menu = "Network Map"
    icon = "icon_map"

    @view(url="^chart/(?P<chart_id>\d+)/$", method=["GET"],
        access="launch", api=True)
    def view_chart(self, request, chart_id):
        chart = self.get_object_or_404(NetworkChart, id=int(chart_id))
        dw = 100
        dh = 50
        ds = 20
        dx = 10
        dy = 10
        r = []
        # Get managed objects
        mos = list(chart.selector.managed_objects)
        mo_ids = [o.id for o in mos]
        # Get links
        if_ids = set(i.id for i in
                  Interface.objects.filter(managed_object__in=mo_ids,
                      type__in=["physical", "management"]))
        links = []
        mo_links = defaultdict(list)  # mo -> [links]
        linked_ports = defaultdict(list)  # link -> [port1, port2]
        for link in Link.objects.filter(interfaces__in=if_ids):
            interfaces = link.interfaces
            if not [i for i in interfaces if i.id not in if_ids]:
                # Both ends on chart
                links += [link]
                for i in interfaces:
                    if i.managed_object not in links:
                        mo_links[i.managed_object] += [link]
        # Attach nodes
        for mo in mos:
            # Fill managed objects
            # Restore state
            state = chart.get_state("mo", mo.id)
            h = state.get("h", dh)
            y = state.get("y")
            if y is None:
                y = dy
                dy += h + ds
            n = {
                "type": "node",
                "id": mo.id,
                "x": state.get("x", dx),
                "y": y,
                "w": state.get("w", dw),
                "h": h,
                "label": mo.name,
                "label_position": state.get("label_position", "s"),
                "shape": "xor",
                "ports": [],
                "address": mo.address,
                "platform": "%s %s" % (mo.get_attr("vendor", ""),
                                       mo.get_attr("platform", "")),
                "version": mo.get_attr("version", "")
            }
            # Used ports
            for link in mo_links[mo]:
                interfaces = [i for i in link.interfaces if i.managed_object == mo]
                p_id = "%d:%s" % (mo.id, link.id)
                if p_id not in linked_ports[link]:
                    n["ports"] += [{
                        "id": p_id,
                        "label": ", ".join(i.name for i in interfaces)
                    }]
                    linked_ports[link] += [p_id]
            #
            r += [n]
        # Attach links
        for link in linked_ports:
            lp = linked_ports[link]
            if len(lp) == 2:
                r += [{
                    "type": "link",
                    "id": str(link.id),
                    "ports": lp
                }]
        return r

    @view(url="^chart/(?P<chart_id>\d+)/$", method=["POST"],
        access="launch", api=True)
    def save_chart(self, request, chart_id):
        chart = self.get_object_or_404(NetworkChart, id=int(chart_id))
        for cmd in json_decode(request.raw_post_data):
            if cmd["type"] == "mo":
                if cmd["cmd"] == "move":
                    chart.update_state("mo", cmd["id"], {
                        "x": cmd["x"],
                        "y": cmd["y"],
                        "w": cmd["w"],
                        "h": cmd["h"]
                    })
                elif cmd["cmd"] == "label_position":
                    chart.update_state("mo", cmd["id"], {
                        "label_position": cmd["label_position"]
                    })
        return True
