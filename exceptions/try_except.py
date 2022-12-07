"""
The try except Python code blocks are
used to handle errors.
"""


def divide():
    while True:
        try:
            num = int(input('Enter a number:'))
            res = 10 / num
            break
        except ValueError:
            print('Not a valid number. Enter again.')
        except ZeroDivisionError:
            print('Your number is zero. Enter again.')
    print(res)

    while True:
        try:
            num = int(input('Enter a number:'))
            res = 10 / num
            break
        except ValueError:
            print("Not a valid number. Enter again.")
    print(res)


divide()
