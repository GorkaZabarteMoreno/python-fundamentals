"""
The Python is (identity operator) checks whether
2 variables/objects point to the same object in memory.

Do not use identity operator while comparing
Python literals.

The Python == (equality operator) checks the value
or equality of 2 variables/objects.
To establish a comparison between instances of a
user defined class, the implementation of __eq__
is needed
"""

equality: bool = 2 == 2
print('Memory address of 2', str(id(2))[0:5], 'and memory address of another', str(id(2))[0:5])
print(equality)


class Obj:

    def __init__(self, num: int):
        self.num = num

    def __eq__(self, other):
        return self.num == other.num


obj1 = Obj(5)
obj2 = Obj(5)
obj3 = obj1

print(obj1 is obj2, 'because', str(id(obj1))[-5:], 'is not the same than', str(id(obj2))[-5:])
print(obj1 is obj3, 'because', str(id(obj1))[-5:], 'is the same than', str(id(obj3))[-5:])
print(obj1 == obj2, 'because', obj1.num, 'is the same than', obj2.num)
