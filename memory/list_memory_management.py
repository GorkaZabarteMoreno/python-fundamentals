"""
See how Python manages memory when a list is created
and modified.
"""

from sys import getsizeof
from typing import Optional


def adding(l: list, num: int, *args) -> None:
    l.append(num)
    if args:
        for n in args:
            l.append(n)
    print('l ->', hex(id(l)), 'with a size of', getsizeof(l), 'and', l)


def removing(l: list) -> None:
    l.pop()
    print('l ->', hex(id(l)), 'with a size of', getsizeof(l), 'and', l)


l1 = [1, 2, 3, 4]
adding(l1, 5)
adding(l1, 6)
adding(l1, 7)
adding(l1, 8)
adding(l1, 9)
adding(l1, 10)
adding(l1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

removing(l1)
removing(l1)
removing(l1)
removing(l1)

