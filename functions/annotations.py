"""
Function annotations are completely optional metadata information about the types used by user-defined functions
"""


def func(n: int, s: str) -> str:
    return 'The number {} is {}'.format(s, n)


if __name__ == '__main__':
    print(func.__annotations__)
