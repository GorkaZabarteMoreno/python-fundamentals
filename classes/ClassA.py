class ClassA:
    """Class A"""
    a: int = 10

    def __init__(self, a: int):
        self.a = a
        pass

    def __init__(self, a1: int, a2: int):
        self.a1 = a1
        self.a2 = a2

    def function(self):
        return "Method of B with " + str(self.a1)


class ClassB:
    """Class B"""
    b: int = 10

    # Python does not support Constructor overload
    def __init__(self, b: int = 5):
        self.b = b


objA = ClassA(10, 20)
objB = ClassB(20)
print(objA.__doc__, objB.__doc__)
print(objB.b)
print(objA.a, objA.a1, objA.a2)

method_object = objA.function
print(ClassA.function(objA))  # Function object is called right away
print(objA.function())  # is the same than ClassA.function(objA)
print(method_object())  # Call the method object whenever you need
