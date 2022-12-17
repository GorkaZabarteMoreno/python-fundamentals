"""
Collection functions:

+ sorted() -> creates a new list
+ reverse() -> creates a new list

+ map()
+ filter()
+ reduce()

They are high order functions because they
can take other functions as arguments, or
they return functions as return value
"""

from functools import reduce

domain: tuple = (1, 2, 3, 4, 5, 6, 7, 8)
image: map = map(lambda num: num * 2, domain)
print(tuple(image))

evens: filter = filter(lambda num: num % 2 == 0, domain)
print(tuple(evens))

suma: int = reduce(lambda acc, num: acc + num, domain, 0)
print(suma)

words = ['Boss', 'alphons', 'Alfred']
print('Sorted without a key argument:', sorted(words))
print('Sorted with a key argument:', sorted(words, key=lambda s: s.lower()))
print('Reverse the list:', list(reversed(words)))

words.sort(key=str.lower, reverse=True)
print('Sort a list inplace in the reverse order:', words)

