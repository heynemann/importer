#!/usr/bin/python
# -*- coding: utf-8 -*-

# importer
# https://github.com/heynemann/importer

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2016 Bernardo Heynemann heynemann@gmail.com

import preggy
from preggy import expect

import importer as importer_mod
from importer.core import Importer

from tests.base import TestCase


class ImporterTestCase(TestCase):
    def test_import_item_should_be_proper_item(self):
        importer = Importer()
        importer.import_item('importer', 'importer.core', 'Importer')
        expect(importer.importer).to_be_instance_of(Importer)

    def test_import_module(self):
        importer = Importer()
        importer.import_item('importer', 'importer')
        expect(importer.importer).to_equal(importer_mod)

    def test_multiple_items_can_be_imported(self):
        importer = Importer()
        importer.import_item(
            key='modules',
            module_names=(
                'preggy',
                'importer'
            )
        )

        expect(importer.modules).to_length(2)
        expect(importer.modules).to_include(preggy)
        expect(importer.modules).to_include(importer_mod)

    def test_multiple_classes_can_be_imported(self):
        importer = Importer()
        importer.import_item(
            key='modules',
            module_names=(
                'importer.core',
                'importer.core',
            ),
            class_name='Importer',
        )

        expect(importer.modules).to_length(2)
        expect(importer.modules[0]).to_equal(Importer)
        expect(importer.modules[1]).to_equal(Importer)

    def test_can_import_and_ignore_errors(self):
        importer = Importer()
        importer.import_item(
            key='module',
            module_names='invalidmodulename',
            ignore_errors=True,
        )
        expect(importer.module).to_be_null()

    def test_import_fails_with_wrong_import(self):
        importer = Importer()

        with expect.error_to_happen(ImportError):
            importer.import_item(
                key='module',
                module_names='invalidmodulename',
            )
