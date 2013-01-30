# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## EdgeCore.ES.get_chassis_id test
## Auto-generated by ./noc debug-script at 27.12.2012 09:41:43
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class EdgeCore_ES_get_chassis_id_Test(ScriptTestCase):
    script = "EdgeCore.ES.get_chassis_id"
    vendor = "EdgeCore"
    platform = "ES4612"
    version = "1.0.6.9"
    input = {}
    result = {'first_chassis_mac': '00:12:CF:7E:0F:30',
 'last_chassis_mac': '00:12:CF:7E:0F:3C'}
    motd = ' \n\n      CLI session with the 8 SFP ports + 4 Gigabit Combo ports L2/L3/L4 managed standalone switch is opened.\n      To end the CLI session, enter [Exit].\n\n'
    cli = {
## 'show version'
'show version': """show version
Unit1
 Serial number          : A751035038
 Hardware version       : R01A
 Number of ports        :12
 Main power status      :up
 Redundant power status :not present

Agent (master)
 Unit ID                : 1
 Loader version         : 2.3.0.2
 Boot ROM version       : 2.2.0.1
 Operation code version : 1.0.6.9""", 
## 'show system'
'show system': """show system
System description: 8 SFP ports + 4 Gigabit Combo ports L2/L3/L4 managed standalone switch
System OID string: 1.3.6.1.4.1.259.6.10.57
System information
 System Up time: 38 days, 6 hours, 7 minutes, and 4.9 seconds
 System Name            : Robespiera4_4612
 System Location        : [NONE]
 System Contact         : [NONE]
 MAC address            : 00-12-CF-7E-0F-30
 Web server             : enable
 Web server port        : 80
 Web secure server      : enable
 Web secure server port : 443
 Telnet server          : enable
 Telnet port            : 23
 Authentication login   :  TACACS local none
 Jumbo Frame :            Disabled 
 POST result              
DUMMY Test 1.................PASS
UART LOOP BACK Test..........PASS
DRAM Test....................PASS
Timer Test...................PASS
PCI Device 1 Test............PASS
I2C bus Initialization.......PASS
RTC Initialization...........PASS
Switch Int Loopback test.....PASS

Done All Pass.""", 
## 'show int statu'
'show int statu': """show int statu
Information of Eth 1/1
 Basic information: 
  Port type: SFP
  Mac address: 00-12-CF-7E-0F-31
 Configuration: 
  Name: (null)
  Port admin: Up
  Speed-duplex: Auto
  Capabilities: 1000full
  Broadcast storm: Enabled
  Broadcast storm limit: 500 packets/second
  Flow control: Disabled
  VLAN Trunking: Disabled
  LACP: Disabled
  Port security: Disabled
  Max MAC count: 0
  Port security action: None
  Combo forced mode: None
 Current status: 
  Link status: Down
  Operation speed-duplex: 1000full
  Flow control type: None

Information of Eth 1/2
 Basic information: 
  Port type: SFP
  Mac address: 00-12-CF-7E-0F-32
 Configuration: 
  Name: (null)
  Port admin: Up
  Speed-duplex: Auto
  Capabilities: 1000full
  Broadcast storm: Enabled
  Broadcast storm limit: 500 packets/second
  Flow control: Disabled
  VLAN Trunking: Disabled
  LACP: Disabled
  Port security: Disabled
  Max MAC count: 0
  Port security action: None
  Combo forced mode: None
 Current status: 
  Link status: Up
  Port operation status: Up
  Operation speed-duplex: 1000full
  Flow control type: None

Information of Eth 1/3
 Basic information: 
  Port type: SFP
  Mac address: 00-12-CF-7E-0F-33
 Configuration: 
  Name: (null)
  Port admin: Up
  Speed-duplex: Auto
  Capabilities: 1000full
  Broadcast storm: Enabled
  Broadcast storm limit: 500 packets/second
  Flow control: Disabled
  VLAN Trunking: Disabled
  LACP: Disabled
  Port security: Disabled
  Max MAC count: 0
  Port security action: None
  Combo forced mode: None
 Current status: 
  Link status: Up
  Port operation status: Up
  Operation speed-duplex: 1000full
 Flow control type: None

Information of Eth 1/4
 Basic information: 
  Port type: SFP
  Mac address: 00-12-CF-7E-0F-34
 Configuration: 
  Name: (null)
  Port admin: Up
  Speed-duplex: Auto
  Capabilities: 1000full
  Broadcast storm: Enabled
  Broadcast storm limit: 500 packets/second
  Flow control: Disabled
  VLAN Trunking: Disabled
  LACP: Disabled
  Port security: Disabled
  Max MAC count: 0
  Port security action: None
  Combo forced mode: None
 Current status: 
  Link status: Up
  Port operation status: Up
 Operation speed-duplex: 1000full
  Flow control type: None

Information of Eth 1/5
 Basic information: 
  Port type: SFP
  Mac address: 00-12-CF-7E-0F-35
 Configuration: 
  Name: (null)
  Port admin: Up
  Speed-duplex: Auto
  Capabilities: 1000full
  Broadcast storm: Enabled
  Broadcast storm limit: 500 packets/second
  Flow control: Disabled
  VLAN Trunking: Disabled
  LACP: Disabled
  Port security: Disabled
  Max MAC count: 0
  Port security action: None
  Combo forced mode: None
 Current status: 
  Link status: Up
 Port operation status: Up
  Operation speed-duplex: 1000full
  Flow control type: None

Information of Eth 1/6
 Basic information: 
  Port type: SFP
  Mac address: 00-12-CF-7E-0F-36
 Configuration: 
  Name: (null)
  Port admin: Up
  Speed-duplex: Auto
  Capabilities: 1000full
  Broadcast storm: Enabled
  Broadcast storm limit: 500 packets/second
  Flow control: Disabled
  VLAN Trunking: Disabled
  LACP: Disabled
  Port security: Disabled
  Max MAC count: 0
  Port security action: None
  Combo forced mode: None
 Current status: 
 Link status: Up
  Port operation status: Up
  Operation speed-duplex: 1000full
  Flow control type: None

Information of Eth 1/7
 Basic information: 
  Port type: SFP
  Mac address: 00-12-CF-7E-0F-37
 Configuration: 
  Name: (null)
  Port admin: Up
  Speed-duplex: Auto
  Capabilities: 1000full
  Broadcast storm: Enabled
  Broadcast storm limit: 500 packets/second
  Flow control: Disabled
  VLAN Trunking: Disabled
  LACP: Disabled
  Port security: Disabled
  Max MAC count: 0
  Port security action: None
  Combo forced mode: None
Current status: 
  Link status: Up
  Port operation status: Up
  Operation speed-duplex: 1000full
  Flow control type: None

Information of Eth 1/8
 Basic information: 
  Port type: SFP
  Mac address: 00-12-CF-7E-0F-38
 Configuration: 
  Name: (null)
  Port admin: Up
  Speed-duplex: Auto
  Capabilities: 1000full
  Broadcast storm: Enabled
  Broadcast storm limit: 500 packets/second
  Flow control: Disabled
  VLAN Trunking: Disabled
  LACP: Disabled
  Port security: Disabled
  Max MAC count: 0
  Port security action: None
 Combo forced mode: None
 Current status: 
  Link status: Up
  Port operation status: Up
  Operation speed-duplex: 1000full
  Flow control type: None

Information of Eth 1/9
 Basic information: 
  Port type: SFP
  Mac address: 00-12-CF-7E-0F-39
 Configuration: 
  Name: (null)
  Port admin: Up
  Speed-duplex: Auto
  Capabilities: 1000full
  Broadcast storm: Enabled
  Broadcast storm limit: 500 packets/second
  Flow control: Disabled
  VLAN Trunking: Disabled
  LACP: Disabled
  Port security: Disabled
  Max MAC count: 0
 Port security action: None
  Combo forced mode: SFP preferred auto
 Current status: 
  Link status: Up
  Port operation status: Up
  Operation speed-duplex: 1000full
  Flow control type: None

Information of Eth 1/10
 Basic information: 
  Port type: 1000T
  Mac address: 00-12-CF-7E-0F-3A
 Configuration: 
  Name: (null)
  Port admin: Up
  Speed-duplex: Auto
  Capabilities: 10half, 10full, 100half, 100full, 1000full
  Broadcast storm: Enabled
  Broadcast storm limit: 500 packets/second
  Flow control: Disabled
  VLAN Trunking: Disabled
  LACP: Disabled
  Port security: Disabled
 Max MAC count: 0
  Port security action: None
  Combo forced mode: SFP preferred auto
 Current status: 
  Link status: Down
  Operation speed-duplex: 1000full
  Flow control type: None

Information of Eth 1/11
 Basic information: 
  Port type: 1000T
  Mac address: 00-12-CF-7E-0F-3B
 Configuration: 
  Name: (null)
  Port admin: Up
  Speed-duplex: Auto
  Capabilities: 10half, 10full, 100half, 100full, 1000full
  Broadcast storm: Enabled
  Broadcast storm limit: 500 packets/second
  Flow control: Disabled
  VLAN Trunking: Disabled
  LACP: Disabled
  Port security: Disabled
 Max MAC count: 0
  Port security action: None
  Combo forced mode: SFP preferred auto
 Current status: 
  Link status: Down
  Operation speed-duplex: 1000full
  Flow control type: None

Information of Eth 1/12
 Basic information: 
  Port type: 1000T
  Mac address: 00-12-CF-7E-0F-3C
 Configuration: 
  Name: (null)
  Port admin: Up
  Speed-duplex: Auto
  Capabilities: 10half, 10full, 100half, 100full, 1000full
  Broadcast storm: Enabled
  Broadcast storm limit: 500 packets/second
  Flow control: Disabled
  VLAN Trunking: Disabled
  LACP: Disabled
  Port security: Disabled
 Max MAC count: 0
  Port security action: None
  Combo forced mode: SFP preferred auto
 Current status: 
  Link status: Up
  Port operation status: Up
  Operation speed-duplex: 1000full
  Flow control type: None

Information of VLAN 1
 MAC address: 00-12-CF-7E-0F-30

Information of VLAN 20
 MAC address: 00-12-CF-7E-0F-30

Information of VLAN 120
 MAC address: 00-12-CF-7E-0F-30

Information of VLAN 733
 MAC address: 00-12-CF-7E-0F-30

Information of VLAN 741
 MAC address: 00-12-CF-7E-0F-30

Information of VLAN 900
 MAC address: 00-12-CF-7E-0F-30

Information of VLAN 2539
 MAC address: 00-12-CF-7E-0F-30
""", 
}
    snmp_get = {}
    snmp_getnext = {}
    http_get = {}
