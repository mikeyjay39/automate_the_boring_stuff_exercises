#!/usr/bin/python3

# password remember program

import sys
import pyperclip

PASSWORDS = {'email': 'email password here',
             'blog': 'blog password here',
             'luggage': 'luggage combination here'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]    # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to the clipboard.')
else:
    print('There is no account named ' + account)
