"""
String is a Python built-in object. It is immutable
"""

str1: str = 'Hello world'
str2: str = "Hello world"
str3: str = """
This is a multiline string
It is commonly used for docstring
"""

print(str1, str2, str3)


def f1(var1: int, var2: str) -> str:
    """
    A docstring is a string literal which
    happens as the first statement of a
    module, function, class, or method definition.
    Such a docstring becomes the __doc__ special
    attribute of that object.

    A package may be documented in the module
    docstring of the __init__.py file
    in the package directory.
    :param var1: explain var1
    :param var2: explain var2
    :return: explain the return
    """
    return 'Function to explain the purpose of a docstring'


print(f1.__doc__)


str4: str = 'It includes a \' single quote'
str5: str = 'It includes a " double quote'
str6: str = "It includes a \" double quote"
str7: str = "It includes a ' single quote"
print(str4, str5, str6, str7, sep='\n')
