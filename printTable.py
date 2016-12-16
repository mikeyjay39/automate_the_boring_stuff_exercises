#! /usr/bin/python3


# Function takes a list of strings and prints out a
# right justified table

def printTable(args):
    colWidths = [0] * len(args[0])
    for i in range(len(args[0])):
        for a in args:
            if len(a[i]) > colWidths[i]:
                colWidths[i] = len(a[i])

    for i in range(len(args[0])):
        for a in args:
            print(a[i].rjust(max(colWidths)), ' ', end='')
        print()

if __name__ == '__main__':
    testData = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]

    printTable(testData)
