"""
Importing Python modules, the interpreter reads
the whole module if the developer used the import
of the whole module.

To avoid this behaviour the __name__ variable can
be used. (Dunder name)
"""

print('Helpers module is being imported')
import helpers

print('Extras module is being imported')
import extras

print('Hiding Entities module is being imported')
from hiding_entities import *
from hiding_entities import __all__

print(__all__)

print(f'The name of the module main.py is {__name__}')

name: str = 'Gorka Zabarte Moreno, 23'
print(f'Lowercase letters: {helpers.extract_lower(name)}')
print(f'Uppercase letters: {helpers.extract_upper(name)}')
print(f'Age: {extras.extract_extra(name)}')
