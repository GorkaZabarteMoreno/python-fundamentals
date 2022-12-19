from packages.src.packages.module1 import get_name
from packages.src.packages.module2 import get_height
from packages.src.packages import *
from packages.src.packages import Point

if __name__ == '__main__':
    app_name: str = 'Gorka App'
    print('{0}'.format(app_name))

    print(f'Name: {get_name()}')
    print(f'Height: {get_height()}')
    p = Point(5.0, 10.0)
    print(p.x, p.y)
