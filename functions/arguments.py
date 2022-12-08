"""
There are the following types of arguments in a Python function:
1. Positional arguments
2. Keyword arguments
3. Default arguments
4. Positional arguments variable
5. Keyword arguments variable

The order in the function call must be:
f(pos_args, *args, kw_args, **kwargs)
"""


def f1(pos1: int, pos2: int, pos3: int) -> str:
    return 'The arguments of this function are positional arguments'


def f2(pos1: int = 5, pos2: int = 17, pos3: int = 23) -> str:
    return 'The arguments of this function are default arguments'


def f3(kw1: int, kw2: int, kw3: int = False, kw4: int = False) -> str:
    return 'The arguments of this function are keyword arguments'


def f4(pos1: int, *args: int, kw1: int, **kwargs: int) -> str:
    print('Sum of positional args: ', pos1 + sum(args))
    print('Sum of keyword args:', kw1 + sum(kwargs.values()))
    return 'The arguments of this function are pos and kw arguments, but variable'



try:
    f1_return: str = f1(1, 2)
except TypeError as e:
    print(e)

try:
    f1_return: str = f1(1, 2, 3)
    f2_return: str = f2(1, 2)
    f3_return: str = f3(kw4=True, kw1=5, kw2=17)
    f4_return: str = f4(5, 17, 23, 100, kw1=1, kw2=2, kw3=3, kw4=4)
    print(f1_return, f2_return, f3_return, f4_return, sep='\n')
except TypeError as e:
    print(e)