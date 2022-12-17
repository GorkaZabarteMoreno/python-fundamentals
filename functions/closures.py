"""
Python treats functions as object and the functions
will be invoked whenever you reference the name,
"""


def greeter(prefix: str):
    def greet(name: str) -> None:
        print(f'{prefix} {name}')

    return greet


hello = greeter('Hello,')
goodbye = greeter('Goodbye,')

hello('Kevin')
goodbye('Kevin')
