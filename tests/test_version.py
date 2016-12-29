#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of importer.
# https://github.com/heynemann/importer

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

from preggy import expect

from importer import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.1.0')
