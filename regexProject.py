#! /usr/bin/python3
# regex program that cleans up text from the clipboard
# TODO(2017/01/16): Create functions and test cases

import pyperclip
import re


class OutOfRangeError(Exception):
    pass


regInput = re.compile(r'[1-4]')
output = ''

# User selects choice
print('What would you like to do with clipboard content?')
print()
print('1) Find website URLs that begin with http:// or https://')
print('2) Clean up dates and replace them with dates in a single format')
print('3) Remove sensitive information eg Social Security & Credit Card')
print('''4) Clean up common typos such as multiple spaces and repeated words \
and punctation''')
print()
userIn = 0

while userIn not in [1, 2, 3, 4]:
    print('Enter your choice 1-4:')
    try:
        userIn = int(input())
    except(ValueError):
        print('Invalid input! Number needed')

text = str(pyperclip.paste())

# Find website URLs that begin with http:// or https://
if userIn == 1:
    urlReg = re.compile(r'((http|https)://\S*\b)')
    mo = []
    for groups in urlReg.findall(text):
        mo.append(groups[0])
    output = '\n'.join(mo)

# Clean up dates and replace them with dates in a single format
if userIn == 2:
    dateReg = re.compile(r'''(
        (\d+)                      # first group
        (-|\.|/)                   # separator
        (\d+)                      # second group
        (-|\.|/)                   # separator
        (\d{2,4})                  # first group
        )''', re.VERBOSE)
    mo = dateReg.search(text)
    if len(mo.group(2)) == 4:
        output = mo.group(4) + '.' + mo.group(6) + '.' \
            + mo.group(2)
    else:
        output = mo.group(2) + '.' + mo.group(4) + '.' \
            + mo.group(6)


# Remove sensitive information eg Social Security & Credit Card
if userIn == 3:
    ccReg = re.compile(r'''(
        \d{15,16}                  # cc number
    )''', re.VERBOSE)
    ssReg = re.compile(r'''(
        \d{3}-?\d{2}-?\d{4}       # social security number
    )''', re.VERBOSE)

    output = text

    for groups in ccReg.findall(text):
        if len(groups) == 15:
            output = ccReg.sub('***************', output)
        if len(groups) == 16:
            output = ccReg.sub('****************', output)

    for groups in ssReg.findall(text):
        if len(groups) == 11:
            output = ssReg.sub('***-**-****', output)
        if len(groups) == 9:
            output = ssReg.sub('***-**-****', output)

# Clean up common typos such as multiple spaces and repeated
# words and punctation
if userIn == 4:
    doubleReg = re.compile(r'''(
    [\s,!?.{2,}]
    )\1+
    ''', re.VERBOSE)

    doubleWord = re.compile(r'''
    (\b\w+\b)\W+\1
    ''', re.VERBOSE)

    output = text

    for groups in doubleReg.findall(output):
        output = doubleReg.sub(r'\1', output)

    for groups in doubleWord.findall(output):
        output = doubleWord.sub(r'\1', output)

# Paste to clipboard
pyperclip.copy(output)
print('Copied to clipboard:')
print(output)
