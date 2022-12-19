"""
Different kind of Python imports

+ Import whole Python module
+ Import whole Python module with an alias
+ Import all the functionalities of a Python module
+ Import a specific functionality of a Python module
+ Import a specific functionality of a Python module
with an alias
"""

import helpers
import helpers as h

from helpers import *
from helpers import extract_lower, extract_upper
from helpers import extract_lower as low, extract_upper as capital

name: str = 'Gorka Zabarte Moreno'

print(f'Lowercase letters: {helpers.extract_lower(name)}')
print(f'Lowercase letters: {h.extract_lower(name)}')
print(f'Lowercase letters: {extract_lower(name)}')
print(f'Lowercase letters: {low(name)}')
