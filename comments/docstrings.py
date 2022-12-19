"""
Docstring to document the module.

+ Inside of modules
+ Inside of functions
+ Inside of classes

The Python interpreter does some actions with
this comment. It allocates space and memory
to the docstring.
"""


def get_name(name: str = 'Gorka') -> str:
    """
    Return the name of the owner of the project

    >>> get_name()
    'Gorka'

    >>> get_name('Paula')
    'Paula'
    """

    return name
