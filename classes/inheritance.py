"""
Python allows multiple inheritance similar to Java interfaces
See Diamond problem
"""


class ClassA:

    def __init__(self, a: int):
        self.a = a


class ClassB:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b


class ClassC(ClassA):

    def __init__(self, a: int, c: int):
        super().__init__(a)
        self.c = c


objC = ClassC(1, 2, 3)
print(objC.a, objC.b, objC.c)
