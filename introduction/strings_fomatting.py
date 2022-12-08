"""
There are two ways to format a Python String:
f'{variable}'
'{variable}'.format(variable=value)
"""

name: str = 'Gorka'
age: int = 23

str_formatted1: str = 'My name is {}'.format(name)
str_formatted2: str = 'My name is {a} and I am {b} years old'.format(a=name, b=age)
print(str_formatted1, str_formatted2, sep='\n')

str_formatted3: str = f'My name is {name}'
str_formatted4: str = f'My name is {name} and I am {age} years old'
print(str_formatted3, str_formatted4)
