# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## DLink.DxS.get_mac_address_table test
## Auto-generated by manage.py debug-script at 2010-12-25 20:03:21
##----------------------------------------------------------------------
## Copyright (C) 2007-2010 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
from noc.lib.test import ScriptTestCase
class DLink_DxS_get_mac_address_table_Test(ScriptTestCase):
    script="DLink.DxS.get_mac_address_table"
    vendor="DLink"
    platform='DGS-3627G'
    version='2.55.B10'
    input={}
    result=[{'interfaces': ['T1'],
  'mac': '00:04:23:D2:EC:88',
  'type': 'D',
  'vlan_id': 25},
 {'interfaces': ['T1'],
  'mac': '00:06:5B:FF:13:B6',
  'type': 'D',
  'vlan_id': 25},
 {'interfaces': ['T1'],
  'mac': '00:08:02:46:97:99',
  'type': 'D',
  'vlan_id': 25},
 {'interfaces': ['T1'],
  'mac': '00:0D:56:BB:75:C2',
  'type': 'D',
  'vlan_id': 25},
 {'interfaces': ['T1'],
  'mac': '00:0E:0C:E5:98:21',
  'type': 'D',
  'vlan_id': 25},
 {'interfaces': ['T1'],
  'mac': '00:0E:0C:E5:98:23',
  'type': 'D',
  'vlan_id': 25},
 {'interfaces': ['T1'],
  'mac': '00:15:17:4E:93:1D',
  'type': 'D',
  'vlan_id': 25},
 {'interfaces': ['T1'],
  'mac': '00:15:17:4E:93:1F',
  'type': 'D',
  'vlan_id': 25},
 {'interfaces': ['T1'],
  'mac': '00:16:76:88:D6:CF',
  'type': 'D',
  'vlan_id': 25},
 {'interfaces': ['T1'],
  'mac': '00:19:D1:E4:F4:F6',
  'type': 'D',
  'vlan_id': 25},
 {'interfaces': ['24'],
  'mac': '00:1B:21:08:C8:98',
  'type': 'D',
  'vlan_id': 25},
 {'interfaces': ['T1'],
  'mac': '00:30:48:86:C7:16',
  'type': 'D',
  'vlan_id': 25},
 {'interfaces': ['T1'],
  'mac': '00:30:48:86:CA:E0',
  'type': 'D',
  'vlan_id': 25},
 {'interfaces': ['T1'],
  'mac': '00:30:48:86:D3:DC',
  'type': 'D',
  'vlan_id': 25},
 {'interfaces': ['T1'],
  'mac': '00:30:48:9F:00:F4',
  'type': 'D',
  'vlan_id': 25},
 {'interfaces': ['T1'],
  'mac': '00:13:49:F2:AD:21',
  'type': 'D',
  'vlan_id': 3500},
 {'interfaces': ['T1'],
  'mac': '00:16:76:88:D6:CF',
  'type': 'D',
  'vlan_id': 3500},
 {'interfaces': ['CPU'],
  'mac': '00:1C:F0:1E:49:00',
  'type': 'S',
  'vlan_id': 3500},
 {'interfaces': ['T1'],
  'mac': '00:06:5B:FF:13:B7',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:08:02:46:97:99',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:0D:56:BB:75:C3',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:15:17:4E:93:1C',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:16:76:88:D6:CF',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['24'],
  'mac': '00:1B:21:08:C8:98',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:1E:37:01',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:1E:38:81',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:1E:3F:C1',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:1E:44:01',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:1E:46:C1',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:1E:47:41',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['CPU'],
  'mac': '00:1C:F0:1E:49:01',
  'type': 'S',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:1E:53:41',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:1E:54:81',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:1E:56:41',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:1E:59:C1',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:1E:5A:C1',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:1E:5C:01',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:27:11:81',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:27:17:41',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:27:23:01',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:27:23:41',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:27:25:C1',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:1C:F0:27:28:41',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:30:48:86:C7:17',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:30:48:86:D3:DC',
  'type': 'D',
  'vlan_id': 3997},
 {'interfaces': ['T1'],
  'mac': '00:30:48:9F:00:F5',
  'type': 'D',
  'vlan_id': 3997}]
    motd=' \n\n                      DGS-3627G Gigabit Ethernet Switch\n                            Command Line Interface\n\n                           Firmware: Build 2.55.B10\n           Copyright(C) 2010 D-Link Corporation. All rights reserved.\n\n'
    cli={
## 'disable clipaging'
'disable clipaging': """disable clipaging
Command: disable clipaging

Success.                                                          
""",
## 'show fdb'
'show fdb': """show fdb
Command: show fdb

 Unicast MAC Address Aging Time  = 300

 VID  VLAN Name                        MAC Address       Port  Type  
 ---- -------------------------------- ----------------- ----- -----------------
 25   Backbone                         00-04-23-D2-EC-88 T1    Dynamic
 25   Backbone                         00-06-5B-FF-13-B6 T1    Dynamic
 25   Backbone                         00-08-02-46-97-99 T1    Dynamic
 25   Backbone                         00-0D-56-BB-75-C2 T1    Dynamic
 25   Backbone                         00-0E-0C-E5-98-21 T1    Dynamic
 25   Backbone                         00-0E-0C-E5-98-23 T1    Dynamic
 25   Backbone                         00-15-17-4E-93-1D T1    Dynamic
 25   Backbone                         00-15-17-4E-93-1F T1    Dynamic
 25   Backbone                         00-16-76-88-D6-CF T1    Dynamic
 25   Backbone                         00-19-D1-E4-F4-F6 T1    Dynamic
 25   Backbone                         00-1B-21-08-C8-98 24    Dynamic
 25   Backbone                         00-30-48-86-C7-16 T1    Dynamic
 25   Backbone                         00-30-48-86-CA-E0 T1    Dynamic
 25   Backbone                         00-30-48-86-D3-DC T1    Dynamic
 25   Backbone                         00-30-48-9F-00-F4 T1    Dynamic
 3500 Management                       00-13-49-F2-AD-21 T1    Dynamic
 3500 Management                       00-16-76-88-D6-CF T1    Dynamic
 3500 Management                       00-1C-F0-1E-49-00 CPU   Self
 3997 OSPF                             00-06-5B-FF-13-B7 T1    Dynamic
 3997 OSPF                             00-08-02-46-97-99 T1    Dynamic
 3997 OSPF                             00-0D-56-BB-75-C3 T1    Dynamic
 3997 OSPF                             00-15-17-4E-93-1C T1    Dynamic
 3997 OSPF                             00-16-76-88-D6-CF T1    Dynamic
 3997 OSPF                             00-1B-21-08-C8-98 24    Dynamic
 3997 OSPF                             00-1C-F0-1E-37-01 T1    Dynamic
 3997 OSPF                             00-1C-F0-1E-38-81 T1    Dynamic
 3997 OSPF                             00-1C-F0-1E-3F-C1 T1    Dynamic
 3997 OSPF                             00-1C-F0-1E-44-01 T1    Dynamic
 3997 OSPF                             00-1C-F0-1E-46-C1 T1    Dynamic
 3997 OSPF                             00-1C-F0-1E-47-41 T1    Dynamic
 3997 OSPF                             00-1C-F0-1E-49-01 CPU   Self
 3997 OSPF                             00-1C-F0-1E-53-41 T1    Dynamic
 3997 OSPF                             00-1C-F0-1E-54-81 T1    Dynamic
 3997 OSPF                             00-1C-F0-1E-56-41 T1    Dynamic
 3997 OSPF                             00-1C-F0-1E-59-C1 T1    Dynamic
 3997 OSPF                             00-1C-F0-1E-5A-C1 T1    Dynamic
 3997 OSPF                             00-1C-F0-1E-5C-01 T1    Dynamic
 3997 OSPF                             00-1C-F0-27-11-81 T1    Dynamic
 3997 OSPF                             00-1C-F0-27-17-41 T1    Dynamic
 3997 OSPF                             00-1C-F0-27-23-01 T1    Dynamic
 3997 OSPF                             00-1C-F0-27-23-41 T1    Dynamic
 3997 OSPF                             00-1C-F0-27-25-C1 T1    Dynamic
 3997 OSPF                             00-1C-F0-27-28-41 T1    Dynamic
 3997 OSPF                             00-30-48-86-C7-17 T1    Dynamic
 3997 OSPF                             00-30-48-86-D3-DC T1    Dynamic
 3997 OSPF                             00-30-48-9F-00-F5 T1    Dynamic

Total Entries: 46

""",
}
    snmp_get={}
    snmp_getnext={}
