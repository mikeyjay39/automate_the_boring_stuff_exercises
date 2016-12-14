#!/usr/bin/python3

''' take the text copied to the clipbaord
    and add a * at the beginning of each line
    '''

import pyperclip

copied = pyperclip.paste()
lines = copied.splitlines()
bulletLine = []

for line in lines:
    bulletLine.append('* ' + line)

pyperclip.copy('\n'.join(bulletLine))
