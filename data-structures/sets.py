"""
A Python set is an unordered data structure where the
elements cannot appear twice.
Hashability makes an object valid as a member of a set.
All of Python’s immutable built-in objects are hashable
and call the function hash().
Objects which are instances of user-defined classes are
hashable by default because they all compare unequal and
their hash value is their id()
"""

s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = set([10, 11, 12, 13, 14, 15])

s1.add(11)

s1.union(s2)
union = s1 | s2

s1.intersection(s2)
intersection = s1 & s2

s1.difference(s2)
difference = s1 - s2

s1.issubset(s2)
issubset = s1 <= s2
issubset_strict = s1 < s2

s1.issuperset(s2)
issuperset = s1 >= s2
issuperset_strict = s1 > s2

s1.isdisjoint(s2)

s1.symmetric_difference(s2)  # neither
symmetric_difference = s1 ^ s2

if 2 in s1:
    print('Membership operation')

s1.pop()

s1.intersection_update(s2)
s1 &= s2

s1.difference_update(s2)
s1 -= s2

s1.symmetric_difference_update(s2)
s1 ^= s2
