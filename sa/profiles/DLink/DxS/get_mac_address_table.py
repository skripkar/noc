# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## DLink.DxS.get_mac_address_table
##----------------------------------------------------------------------
## Copyright (C) 2007-2010 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
""" 
""" 
from noc.sa.script import Script as NOCScript
from noc.sa.interfaces import IGetMACAddressTable
from noc.sa.profiles.DLink.DxS import DGS3600
import re

class Script(NOCScript):
    name="DLink.DxS.get_mac_address_table"
    implements=[IGetMACAddressTable]
    rx_line=re.compile(r"^\s*(?P<vlan_id>\d+)\s+\S+\s+(?P<mac>\S+)\s+(?P<interfaces>\S+)\s+(?P<type>\S+)\s*$",re.MULTILINE)
    def execute(self,interface=None,vlan=None,mac=None):
        cmd="show fdb" 
        if mac is not None:
            cmd+=" mac_address %s"%mac
        if interface is not None:
            cmd+=" port %s"%interface
        if vlan is not None:
	    # Will be work in future releases
	    #if self.match_version(DGS3600, version__gte="2.52"):
	    v=self.scripts.get_version()
	    if DGS3600(v) and self.profile.cmp_version(v["version"],"2.52")>0:
		cmd+=" vlanid %d"%vlan
	    else:
		for v in self.scripts.get_vlans():
            	    if v["vlan_id"]==vlan:
    			cmd+=" vlan %s"%v["name"]
    			break
        macs=self.cli(cmd)
        r=[]
        for match in self.rx_line.finditer(macs):
            r+=[{
                "vlan_id"   : match.group("vlan_id"),
                "mac"       : match.group("mac"),
                "interfaces": [match.group("interfaces")],
                "type"      : {"dynamic":"D","static":"S","deleteontimeout":"D","deleteonreset":"D","permanent":"S","self":"S"}[match.group("type").lower()],
            }]
        return r
