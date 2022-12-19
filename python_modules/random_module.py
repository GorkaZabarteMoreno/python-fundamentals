"""
Random module
+ random.random() is the base for all randomness
It returns a float between 0.0 and 1.0

+ random.seed() for predictable randomness

+ choice - random element of a sequence
+ sample - returns a subset of length N
+ shuffle (mutable datatypes) -
"""

import random

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pick = random.choice(l1)
sample = random.sample(l1, 3)
random.shuffle(l1)

print(pick, sample, l1)