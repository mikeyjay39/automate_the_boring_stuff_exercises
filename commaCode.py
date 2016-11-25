#!/usr/bin/python3


import sys


def commaFunc(myList):
    return ', '.join(myList).lstrip(', ')

if __name__ == '__main__':
    spam = []
    if len(sys.argv) == 1:
        # spam = ['apples', 'bananas', 'tofu', 'cats']
        print('Enter list items. Type "quit" when you are finished')
        item = ''
        while item != 'quit':
            spam.append(item)
            item = input()
        print(commaFunc(spam))
    else:
        for i in sys.argv:
            spam.append(i)
        del spam[0]
        print(commaFunc(spam))
