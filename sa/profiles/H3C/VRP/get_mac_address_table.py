# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## H3C.VRP.get_mac_address_table
##----------------------------------------------------------------------
## Copyright (C) 2007-2009 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""
"""
## Python modules
import re
## NOC modules
from noc.sa.script import Script as NOCScript
from noc.sa.interfaces import IGetMACAddressTable, IGetVersion

rx_vrp3line=re.compile(r"^(?P<mac>\S+)\s+(?P<vlan_id>\d+)\s+(?P<type>Learned|Config static)\s+(?P<interfaces>[^ ]+)\s{2,}")
rx_vrp5line=re.compile(r"^(?P<mac>\S+)\s+(?P<vlan_id>\d+)\s+(?:\S+)\s+(?:\S+)\s+(?P<interfaces>\S+)\s+(?P<type>dynamic|static)\s+")
##
## H3C.VRP.get_mac_address_table
##
class Script(NOCScript):
    name="H3C.VRP.get_mac_address_table"
    implements=[IGetMACAddressTable]
    requires=[("get_version",IGetVersion)]
    def execute(self,interface=None,vlan=None,mac=None):
        cmd="display mac-address"
        if mac is not None:
            cmd+=" %s"%self.profile.convert_mac(mac)
        version=self.scripts.get_version()["version"].split(".")[0]
        rx_line=rx_vrp3line
#        if version=="3":
#            rx_line=rx_vrp3line
#        elif version=="5":
#            rx_line=rx_vrp5line
        r=[]
        for l in self.cli(cmd).splitlines():
            match=rx_line.match(l.strip())
            if match:
                if vlan is not None and int(match.group("vlan_id"))!=vlan:
                    continue
                if interface is not None and match.group("interfaces")!=interface:
                    continue
                r+=[{
                    "vlan_id"   : match.group("vlan_id"),
                    "mac"       : match.group("mac"),
                    "interfaces": [match.group("interfaces")],
                    "type"      : {"dynamic":"D","static":"S","learned":"D","Config static":"S"}[match.group("type").lower()],
                }]
        return r
