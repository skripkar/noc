# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Zyxel.ZyNOS.ping test
## Auto-generated by ./noc debug-script at 2011-07-01 17:06:59
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Zyxel_ZyNOS_ping_Test(ScriptTestCase):
    script = "Zyxel.ZyNOS.ping"
    vendor = "Zyxel"
    platform = 'GS-3012'
    version = '3.80(LH.2)'
    input = {'address': '192.168.4.19'}
    result = {'avg': 0, 'count': 6, 'max': 10, 'min': 0, 'success': 6}
    motd = ' ****\nCopyright (c) 1994 - 2008 ZyXEL Communications Corp.\n'
    cli = {
## 'ping 192.168.4.19'
'ping 192.168.4.19': """ ping 192.168.4.19
Resolving 192.168.4.19... 192.168.4.19
 sent  rcvd  rate    rtt     avg    mdev     max     min  reply from
    1     1  100       0       0       0       0       0  192.168.4.19
    2     2  100       0       0       0       0       0  192.168.4.19
    3     3  100      10       1       3      10       0  192.168.4.19""", 
}
    snmp_get = {}
    snmp_getnext = {}
