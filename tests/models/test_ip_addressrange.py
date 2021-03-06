# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# ip.AddressRange tests
# ----------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
from __future__ import absolute_import
# NOC modules
from .base import BaseModelTest
from noc.ip.models.addressrange import AddressRange


class TestTestIpAddressRange(BaseModelTest):
    model = AddressRange
