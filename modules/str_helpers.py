"""
Str helper module with functions to
facilitate the work with strings
"""

import random


def reverse(name: str) -> str:
    # return name[::-1]
    length: int = len(name)
    name_reversed: str = ''
    for i in range(length - 1, -1, -1):
        name_reversed += name[i]
    return name_reversed


def shuffle(name: str) -> str:
    name_list = list(name)
    random.shuffle(list(name_list))
    return ''.join(name_list)
