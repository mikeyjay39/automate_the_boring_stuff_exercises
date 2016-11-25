#!/usr/bin/python3


def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

if __name__ == '__main__':
    number = ''

    while not isinstance(number, int):
        print('Enter number: ')
        try:

            number = int(input())
        except Exception:
            print('Invalid input')

    while number != 1:
        number = abs(collatz(number))
        print(number)
