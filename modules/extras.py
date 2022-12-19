print('Extras module')

print(f'The name of the extras.py module is {__name__}')


def extract_extra(phrase: str):
    """Extract extra information"""
    return phrase[-3:]
