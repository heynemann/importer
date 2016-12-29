# importer

Importer is a library to do dynamic importing of modules in python.

## Installing

```
    $ pip install importer-lib
```

## Usage

```
from importer import Importer

# sets importer.module_a to the sys module
importer.import_item('module_a', 'sys')

# sets importer.module_b to the importer.core module
importer.import_item('module_b', 'importer.core')

# sets importer.module_c to the Importer class
importer.import_item('module_c', 'importer.core', class_name='Importer')

# Multiple Imports

# sets importer.modules to the specified modules
importer.import_item('modules', ('importer.core', 'os', 'sys', 'preggy'))

# sets importer.handlers to the the specified class in all modules
# this is very useful for modules that have the
# same class like request handlers (Handler class)
importer.import_item(
    'handlers', (
        'module.handlers.healthcheck',
        'module.handlers.index',
        'module.handlers.login',
    ), class_name='Handler'
)
