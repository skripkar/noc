# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# NTP server host
# ---------------------------------------------------------------------
# Copyright (C) 2007-2015 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# NOC modules
from __future__ import absolute_import
from .base import BaseFact


class NTPServer(BaseFact):
    ATTRS = ["ip"]
    ID = ["ip"]

    def __init__(self, ip=None):
        super(NTPServer, self).__init__()
        self.ip = ip

    def __unicode__(self):
        return "NTPServer %s" % self.ip

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value or None
