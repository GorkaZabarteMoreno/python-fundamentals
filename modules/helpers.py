"""
Python modules

Everything with a name entity can be
used from this module
"""

print('Helpers module')

print(f'The name of the module helpers.py is {__name__}')


def extract_upper(phrase: str):
    """Extract capital letters of a string"""

    return list(filter(str.isupper, phrase))


def extract_lower(phrase: str) -> list:
    """Extract lower letters of a string"""

    return list(filter(str.islower, phrase))


if __name__ == '__main__':
    print('Inside the helpers.py main module ')

print('End of Helpers module')
