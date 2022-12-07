try:
    file1 = open("example.txt")
    for line in file1:
        print(line)

    num: float = int(input('Enter a number:'))
    div = num/100
except ZeroDivisionError:
    print('Error')
finally:
    file1.close()
