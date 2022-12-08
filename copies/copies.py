"""
The differences between a shallow copy and a deep copy:
It is very important the difference between mutable and
immutable objects because immutable objects have always the
same memory address.

+ An assignment just create a new reference to the
same memory address.
+ A shallow copy creates a new memory address, but with the same
references than the previous object.
+ A deep copy create a new variable with a different memory address and
creates new objects for the mutable objects inside.
"""

from copy import deepcopy, copy

# Mutable
obj1 = [1, 2, 3, 4, [1, 2]]
obj2 = obj1
obj3 = copy(obj1)
obj4 = deepcopy(obj1)

print(str(id(obj1)), str(id(obj2)), str(id(obj3)), str(id(obj4)), sep='\n')
print(str(id(obj1[4])), str(id(obj2[4])), str(id(obj3[4])), str(id(obj4[4])), sep='\n')


obj5 = (1, 2, 3, 4, (1, 2))
obj6 = obj5
obj7 = copy(obj5)
obj8 = deepcopy(obj5)

print(str(id(obj5)), str(id(obj6)), str(id(obj7)), str(id(obj8)), sep='\n')
print(str(id(obj5[4])), str(id(obj6[4])), str(id(obj7[4])), str(id(obj8[4])), sep='\n')