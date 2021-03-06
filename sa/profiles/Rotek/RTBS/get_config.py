# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Rotek.RTBS.get_config
# ---------------------------------------------------------------------
# Copyright (C) 2007-2017 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetconfig import IGetConfig


class Script(BaseScript):
    name = "Rotek.RTBS.get_config"
    interface = IGetConfig

    def execute(self):
        config = self.cli("show config")
        return self.cleaned_config(config)
