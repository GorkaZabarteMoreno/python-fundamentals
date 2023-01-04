"""
A Python dictionary is a key:value data structure.
Hashability makes an object usable as a dictionary key.
All of Python’s immutable built-in objects are hashable
and call the function hash().
Objects which are instances of user-defined classes are
hashable by default because they all compare unequal and
their hash value is their id()

Hashable is used to create high performance,
pseudo random access data structures where
large amount of data is needed to be stored and accessed quickly.
"""

from types import MappingProxyType

d1 = {
    'Name': 'Gorka',
    'Surname': 'Zabarte',
    'Sex': 'M',
    'Age': 23,
    'Height': 175.43,
    'Weight': 75.4,
    'BMI': 7.5
}

d1.items()
d1.keys()
d1.values()

d1.pop('Name')
d1.get('Name')
d1.get('Surname')
d2 = d1.fromkeys(['Age', 'Height', 'Weight'], 23)
d1.setdefault('Age', 24)
d3 = d1.copy()
d1.clear()

immutable_dict = MappingProxyType(
    {
        "Kevin": 9001,
        "Benny": 8000,
    }
)


def f(c: str):
    if c == 'a':
        return 1
    elif c == 'b':
        return 2
    elif c == 'c':
        return 3
    else:
        return -1


def dict_comprehension(letters: tuple = ('a', 'b', 'c')):
    return {letter: f(letter) for letter in letters}


print(dict_comprehension())
