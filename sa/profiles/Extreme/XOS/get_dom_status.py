# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Extreme.XOS.get_dom_status
# ---------------------------------------------------------------------
# Copyright (C) 2007-2012 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
import re
# NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetdomstatus import IGetDOMStatus
from noc.lib.text import parse_kv
from noc.lib.validators import is_int
from noc.lib.convert import mw2dbm


class Script(BaseScript):
    name = "Extreme.XOS.get_dom_status"
    interface = IGetDOMStatus

    rx_trans_split = re.compile(r"Port\s+(\S+)\n")
    rx_no_trans = re.compile(r"No ([\S\+\/]+) detected\.")

    def normalize_output(self, out):
        if out and len(out.split()) == 3:
            val, mea, he = out.split()
        else:
            self.logger.warning("Unknown output format value: %s, skipping" % out)
            return None
        if mea == "uW":
            val = mw2dbm(float(val) / 1000.0)
        elif mea == "uA":
            val = float(val) / 1000.0
        elif mea == "V":
            val = val / 1000.0
        return val

    def execute_cli(self, interface=None):
        # @todo without stack slot (Members | Ids)
        # show ports transceiver information
        cmd = "debug hal show optic-info ddmi"
        if interface is not None:
            cmd = "debug hal show optic-info ddmi slot %s port %s" % interface.split(":")
        try:
            v = self.cli(cmd)
        except self.CLISyntaxError:
            return []
        port = None
        r = []
        k_map = {"temperature": "temp_c",
                 "voltage": "voltage_v",
                 "tx bias": "current_ma",
                 "tx power": "optical_tx_dbm",
                 "rx power": "optical_rx_dbm"
                 }
        for block in self.rx_trans_split.split(v):
            if is_int(block):
                port = block.strip()
                continue
            if self.rx_no_trans.match(block) or not port:
                continue
            d = parse_kv(k_map, block)

            r += [{
                "interface": port,
                "temp_c": self.normalize_output(d.get("temp_c")),
                "voltage_v": self.normalize_output(d.get("voltage_v")),
                "current_ma": self.normalize_output(d.get("current_ma")),
                "optical_rx_dbm": self.normalize_output(d.get("optical_rx_dbm")),
                "optical_tx_dbm": self.normalize_output(d.get("optical_tx_dbm"))
            }]
        return r