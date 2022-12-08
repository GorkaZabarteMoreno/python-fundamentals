"""
See how Python manages memory when a tuple is created.

As it is an immutable data structure it does not need to
create additional memory. It is more efficiency in terms of
memory management.
"""
import sys
from sys import getsizeof
from typing import Optional

t1 = (1, 2, 3, 4, 5)
print('t1 ->', hex(id(t1)), 'with a size of', getsizeof(t1), 'and', t1)