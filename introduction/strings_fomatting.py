"""
There are 4 ways to format a Python String:
'%s' % variable
'%(variable)s' % {'variable': value}
f'{variable}'
'{variable}'.format(variable=value)
"""

from string import Template

name: str = 'Gorka'
age: int = 23

str_formatted1: str = 'My name is {}'.format(name)
str_formatted2: str = 'My name is {a} and I am {b} years old'.format(a=name, b=age)
str_hex1: str = 'My name is {a} and I am 0x{b:x} hexadecimal years old'.format(a=name, b=age)
print(str_formatted1, str_formatted2, str_hex1, sep='\n')

str_formatted3: str = f'My name is {name}'
str_formatted4: str = f'My name is {name} and I am {age} years old'
str_hex2: str = f'My name is {name} and I am {age:#x} hexadecimal years old'
print(str_formatted3, str_formatted4, str_hex2, sep='\n')

str_formatted5: str = 'My name is %s' % name
str_formatted6: str = 'My name is %s and I am %d years old' % (name, age)
print(str_formatted5, str_formatted6, sep='\n')

str_formatted7: str = 'My name is %(name)s' % {'name': name}
str_formatted8: str = 'My name is %(name)s and I am %(age)d years old' % \
                      {'name': name, 'age': age}
print(str_formatted7, str_formatted8, sep='\n')

str_template: Template = Template('My name is $name and I am $age years old')
print(str_template.substitute(name=name, age=age))
