# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# peer.ASSet tests
# ----------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
from __future__ import absolute_import
# NOC modules
from .base import BaseModelTest
from noc.peer.models.asset import ASSet


class TestTestPeerASSet(BaseModelTest):
    model = ASSet
