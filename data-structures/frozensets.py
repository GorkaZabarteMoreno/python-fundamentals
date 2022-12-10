"""
A Python frozenset is a built-in type which it is exactly
a set, but it is immutable.
"""

f1 = frozenset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(id(f1))

f1 &= {1, 2, 3}
print(f1, id(f1), sep='\n')  # It is another object

