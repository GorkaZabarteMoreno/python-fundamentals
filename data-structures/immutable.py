"""
In Python everything is an object. An all the
objects have its internal state. The fact that
some of those do not allow the developer to change
its state makes them immutable objects.

Immutable objects are numbers, strings, tuples, frozenset
User defined classes can be immutable
"""

t1 = (1, 2, 3, 4, 5)
try:
    t1[5] = 5.5
except TypeError as e:
    print(e)
