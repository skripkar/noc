# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## DLink.DGS3100.get_chassis_id test
## Auto-generated by ./noc debug-script at 2011-10-14 11:54:47
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class DLink_DGS3100_get_chassis_id_Test(ScriptTestCase):
    script = "DLink.DGS3100.get_chassis_id"
    vendor = "DLink"
    platform = 'DGS-3100-24TG'
    version = '3.00.43'
    input = {}
    result = '00:24:01:30:D3:5D'
    motd = '******\n\n'
    cli = {
## 'show switch'
'show switch': """ show switch

Device Type         : DGS-3100-24TG  Gigabit stackable L2 Managed Switch
MAC Address         : 00:24:01:30:d3:5d
IP Address          : 10.116.0.91
VLAN Name           : upr
Subnet Mask         : 255.255.0.0
Default Gateway     : 10.116.0.1
Boot PROM Version   : 1.0.1.04
Firmware Version    : 3.00.43
Hardware Version    : 04
Serial Number       : F3Q318C000636(unit 1)
                      F3Q3299000059(unit 2)
System Name         : SV
System Location     : SV
System Contact      : 
Spanning Tree       : Disabled
GVRP                : Disabled
IGMP Snooping       : Disabled
TELNET              : Enabled
WEB                 : Disabled
""", 
}
    snmp_get = {}
    snmp_getnext = {}
