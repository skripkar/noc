# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# DLink.DVG.get_version
# ---------------------------------------------------------------------
# Copyright (C) 2007-2011 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
import re
# NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetversion import IGetVersion


class Script(BaseScript):
    name = "DLink.DVG.get_version"
    interface = IGetVersion
    cache = True

    rx_platform = re.compile(
        r"^Software \[(==|\S+ ==) Ver\(+(?P<version>\S+)\s+\S+\s+\S+\)\s+"
        r"PId\(+\S+\)\s+Drv\(+\S+\)\s+Hw\(+(?P<platform>\S+)+\) "
        r"(== |== (?P<hardware>\S+))+\]$",
        re.MULTILINE)

    platforms_cli = {
        "??????": "DVG-2101S",
        "DSA": "DVG-2102S",
        "PNP1632-32": "DVG-4032S",
        "SA7S4": "DVG-5004S",
        "TSO": "DVG-7111S"
    }

    platforms_snmp = {
        "3.2.10": "DVG-2101S",
        "???": "DVG-2102S",
        "?.??": "DVG-4032S",
        "1.2.1": "DVG-5004S",
        "?.?.?": "DVG-7111S"
    }

    def execute_snmp(self, **kwargs):
        platform = self.snmp.get("1.3.6.1.2.1.1.2.0", cached=True)
        platform = platform.split(', ')
        line = len(platform) - 1
        try:
            platform = (platform[line - 2] + '.' + platform[line - 1] +
                        '.' + platform[line])
            platform = self.platforms_snmp.get(platform.split(')')[0],
                                               '????')
            version = "1.02.38.x"
        except Exception:
            platform = "DVG-N5402G"
            version = self.snmp.get("1.3.6.1.2.1.1.1.0", cached=True)
            version = version.split()[2]
        return {
            "vendor": "DLink",
            "platform": platform,
            "version": version,
        }

    def execute_cli(self):
        # Try SNMP first
        if self.has_snmp():
            try:
                return self.execute_snmp()
            except self.snmp.TimeOutError:
                pass

        # Fallback to CLI
        plat = self.cli("GET STATUS HARDWARE", cached=True)
        match = self.rx_platform.search(plat)
        platform = self.platforms_cli.get(match.group("platform"), '????')
        r = {
            "vendor": "DLink",
            "platform": platform,
            "version": match.group("version")
        }
        if match.group("hardware"):
            r["attributes"]["HW version"] = match.group("hardware")
        return r
