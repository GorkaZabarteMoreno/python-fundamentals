"""
Python example module to add in
PYTHONPATH environment variable

1. Check standard library first
2. Check the directories in sys.path
"""
from os import getenv


def get_env_vars(env_var: str) -> None:
    print(f'You have the following env variables {getenv(key=env_var)}')


get_env_vars('BRS')
