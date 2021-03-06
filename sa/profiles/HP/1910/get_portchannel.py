# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# HP.1910.get_portchannel
# ---------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
import re
# NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetportchannel import IGetPortchannel


class Script(BaseScript):
    name = "HP.1910.get_portchannel"
    interface = IGetPortchannel

    rx_po = re.compile(r"^Aggregation Interface: Bridge-Aggregation(?P<port>\d+)$", re.MULTILINE)
    rx_type = re.compile(r"^Aggregation Mode: (?P<type>\S+)$", re.MULTILINE)
    rx_iface = re.compile(r"^\s+(?P<interface>\S+)\s+(S|U)\s+\d+\s+\d", re.MULTILINE)

    def execute_cli(self):
        r = []
        data = self.cli("display link-aggregation verbose").split('\n')
        L = len(data) - 1
        i = 0
        while i < L:
            raw = data[i]
            match = self.rx_po.search(raw)
            while not match:
                if i == L:
                    break
                i += 1
                raw = data[i]
                match = self.rx_po.search(raw)
            if i == L:
                break
            port = 'Po' + match.group("port")
            i += 1
            raw = data[i]
            match = self.rx_type.search(raw)
            while not match:
                i += 1
                raw = data[i]
                match = self.rx_type.search(raw)
            typ = match.group("type")
            i += 1
            raw = data[i]
            match = self.rx_iface.search(raw)
            members = []
            while not match:
                i += 1
                raw = data[i]
                match = self.rx_iface.search(raw)
            while match:
                members.append(match.group("interface").replace('GE', 'gi'))
                i += 1
                raw = data[i]
                match = self.rx_iface.search(raw)

            r += [
                {
                    "interface": port,
                    "type": "L" if typ == "Dynamic" else "S",
                    "members": members,
                }
            ]

        return r

    def execute_snmp(self):
        r = []
        if self.has_snmp():
            try:
                for v in self.snmp.get_tables(
                    ["1.2.840.10006.300.43.1.1.1.1.6", "1.2.840.10006.300.43.1.1.2.1.1",
                     "1.2.840.10006.300.43.1.1.1.1.5"], bulk=True):
                    port = 'Po' + str(v[1])
                    s = self.hex_to_bin(v[2])
                    members = []
                    for i in range(len(s)):
                        if s[i] == '1':
                            oid = "1.3.6.1.2.1.31.1.1.1.1." + str(i + 1)
                            iface = self.snmp.get(oid, cached=True)  # IF-MIB
                            members.append(iface)

                    r.append(
                        {
                            "interface": port,
                            # ?????? type detection
                            # 1.2.840.10006.300.43.1.1.1.1.5 is correct???????????
                            "type": "L" if v[3] == '1' else "S",
                            "members": members,
                        }
                    )
                return r
            except self.snmp.TimeOutError:
                pass
