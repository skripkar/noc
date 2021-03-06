# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# cm.ObjectNotify tests
# ----------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
from __future__ import absolute_import
# NOC modules
from .base import BaseModelTest
from noc.cm.models.objectnotify import ObjectNotify


class TestTestCmObjectNotify(BaseModelTest):
    model = ObjectNotify
