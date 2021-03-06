# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Raisecom.ROS.get_tech_support
# ---------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------
"""
"""
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igettechsupport import IGetTechSupport


class Script(BaseScript):
    name = "Raisecom.ROS.get_tech_support"
    interface = IGetTechSupport

    def execute_cli(self):
        try:
            c = self.cli("show tech-support")
        except self.CLISyntaxError:
            raise self.NotSupportedError()
        return unicode(c, "utf8", "ignore").encode("utf8")
