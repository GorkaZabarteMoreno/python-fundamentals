"""
A Python list is an indexed, sequential and mutable object.
A Python list stores its information in contiguous memory locations.
"""

l1 = [3, 7, 1, 4, 9, 10, 2, 6, 5, 8]
t1 = (10, 11, 12)

l1.index(2)
l1.sort()
l1.append(11)
l1.pop()
l1.pop(9)
l1.insert(0, 0)
if 5 in l1:
    print('Operator in has O(n) complexity')
l1.extend(t1)
l1.count(0)