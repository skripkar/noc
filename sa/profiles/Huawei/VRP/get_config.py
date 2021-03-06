# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Huawei.VRP.get_config
# ---------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------
"""
"""
# NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetconfig import IGetConfig


class Script(BaseScript):
    name = "Huawei.VRP.get_config"
    interface = IGetConfig

    def execute(self):
        self.cli("undo terminal monitor", ignore_errors=True)
        config = self.cli("display current-configuration")
        config = self.profile.clean_spaces(config)
        return self.cleaned_config(config)
