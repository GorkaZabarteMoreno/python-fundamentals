"""
A Python tuple is an indexed, sequential and immutable data structure.
A Python tuple stores its information in contiguous memory locations.
"""

t1 = (3, 7, 1, 4, 9, 10, 2, 6, 5, 8)

t1.count(0)
t1.count(1)

t1 = t1 + (0, )
if 5 in t1:
    print('Operator in has O(n) complexity')

t1.index(0)