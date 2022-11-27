def generator():
    yield 'Hola 1'
    yield 'Hola 2'
    yield 'Hola 3'


if __name__ == '__main__':
    for i in generator():
        print(i)
