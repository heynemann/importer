#!/usr/bin/python
# -*- coding: utf-8 -*-

# importer
# https://github.com/heynemann/importer

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2016 Bernardo Heynemann heynemann@gmail.com

import logging
from functools import reduce


def import_class(name, get_module=False):
    module_name = get_module and name or '.'.join(name.split('.')[:-1])
    klass = name.split('.')[-1]

    module = get_module and __import__(name) or __import__(module_name)
    if '.' in module_name:
        module = reduce(getattr, module_name.split('.')[1:], module)

    return get_module and module or getattr(module, klass)


class Importer:
    def import_class(self, name, get_module=False):
        return import_class(name, get_module)

    def try_import(self, module_name, class_name, ignore_errors):
        try:
            if class_name is not None:
                module = self.import_class('%s.%s' % (module_name, class_name))
            else:
                module = self.import_class(module_name, get_module=True)

            return module
        except ImportError as e:
            if ignore_errors:
                logging.warn('Module %s could not be imported: %s', module_name, e)
                return None
            else:
                raise e

    def import_item(self, key, module_names, class_name=None, ignore_errors=False):
        is_multiple = isinstance(module_names, (list, tuple))
        if is_multiple:
            modules = []
            for module_name in module_names:
                module = self.try_import(module_name, class_name, ignore_errors)
                modules.append(module)
            setattr(self, key.lower(), tuple(modules))
        else:
            module = self.try_import(module_names, class_name, ignore_errors)
            setattr(self, key.lower(), module)

    def load(self, *modules):
        for module in modules:
            key = module['key']
            module_names = module['module_names']

            class_name = None
            if 'class_name' in module:
                class_name = module['class_name']

            ignore_errors = False
            if 'ignore_errors' in module:
                ignore_errors = module['ignore_errors']

            self.import_item(key, module_names, class_name, ignore_errors)
