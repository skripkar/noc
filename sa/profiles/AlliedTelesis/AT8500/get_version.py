# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# AlliedTelesis.AT8500.get_version
# ---------------------------------------------------------------------
# Copyright (C) 2007-2010 The NOC Project
# coded by azhur
# See LICENSE for details
# ---------------------------------------------------------------------
"""
"""
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetversion import IGetVersion
import re


class Script(BaseScript):
    name = "AlliedTelesis.AT8500.get_version"
    cache = True
    interface = IGetVersion
    rx_ver = re.compile(
        r"^Model Name \.+ (?P<platform>AT[/\w-]+).+^Application \.+ "
        r"ATS62 v(?P<version>[\d.]+)", re.MULTILINE | re.DOTALL)

    def execute(self):
        if self.has_snmp():
            try:
                pl = self.snmp.get("1.3.6.1.4.1.207.8.17.1.3.1.6.1")
                ver = self.snmp.get("1.3.6.1.4.1.207.8.17.1.3.1.5.1")
                return {
                    "vendor": "Allied Telesis",
                    "platform": pl,
                    "version": ver.lstrip("v"),
                }
            except self.snmp.TimeOutError:
                pass
        v = self.cli("show system")
        match = self.rx_ver.search(v)
        return {
            "vendor": "Allied Telesis",
            "platform": match.group("platform"),
            "version": match.group("version"),
        }
