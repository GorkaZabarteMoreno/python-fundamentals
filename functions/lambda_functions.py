"""
Lambda functions are anonymous functions, and
they are useful when it is a repeatable code, but
it is not worth to create a function.

It is a quick, easy and in line.

The differences between lambda function and
common functions definitions are:

+ Lambda functions are anonymous
+ Lambda functions only have one expression
+ Lambda functions can be assigned to a variable
"""


def f_name(a: int, b: int) -> int:
    print('Function content')
    return a + b


def square(num: int) -> int:
    """Square of a number"""
    return num * num


square_lambda = lambda num: num * num

assert square(4) == square_lambda(4)

add_lambda = lambda num1, num2: num1 + num2
