"""
In Python everything is an object. An all the
objects have its internal state. The fact that
some of those allow the developer to change
its state makes them mutable objects.

Mutable objects are lists, sets, dictionaries
User defined classes can be mutable
"""

l1 = [1, 2, 3, 4, 5]
l1[4] = 5.5
print(l1)
