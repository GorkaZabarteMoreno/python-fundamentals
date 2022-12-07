# 0. Write a code for getting the middle letters of even or odd length strings
def get_middle(s: str) -> str:
    lenght, middle = len(s), int(len(s) / 2)
    if lenght % 2 == 0:
        return s[middle - 1:middle + 1]
    else:
        return s[middle]

# 1. Write a code for swapping values of variables

a = 5
b = 10
# Expected result: a = 10; b = 5
a, b = b, a
(a, *b) = (b, a, 1)
print(b)
print(a, b)


# --------------------------------------------------------------------------------------

# 2. Write a function that takes a single argument.
# Function shall return True if this argument is a list of strings and False otherwise.
def func(arg):
    if type(arg) is not list:
        return False
    for element in arg:
        if type(element) is not str:
            return False
    return True


def func2(arg2):
    return type(arg2) is list and all([type(e) is str for e in arg2])


# --------------------------------------------------------------------------------------

# 3. Write a function that takes any amount of arguments.
# Function shall return an amount of provided arguments.
def func3(*args):  # func(1, 2, 3, 4) -> 4
    print(len(args))  # tuple 
    return len(args)


# --------------------------------------------------------------------------------------

# 4. Remove duplicate elements from a list while preserving order.
def func4(arr):
    aux = []
    for e in arr:
        if e not in aux:
            aux.append(e)
    return aux


def func5(arr):
    return list(dict.fromkeys(arr))

# Example:
# Input array: [3, 1, 2, 3, 4, 2, 2, 5]
# Output array: [3, 1, 2, 4, 5]
