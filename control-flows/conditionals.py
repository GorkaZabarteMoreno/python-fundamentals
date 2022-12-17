"""
The if conditional expression
"""
CONDITION = True
var = 1 if CONDITION else 0
print('A') if CONDITION else print('B')


def f1():
    print('Function 1')


def f2():
    print('Function 2')


f1() if CONDITION else f2()
