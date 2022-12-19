"""
Everything inside a Python module is
accessible outside the module if it's name
is known.

Exceptions:
+ Use __all__ variable with import *
+ Use _name to make it semi-private
"""

print(f'The name of the hiding_entities is {__name__}')

__all__ = ['func1', 'VAR_G']

VAR_G: int = 10

if __name__ == '__main__':
    print(__all__)


def func1(num: int) -> int:
    return num + VAR_G


def _func2(num: int) -> int:
    return num * VAR_G
