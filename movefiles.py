#! /usr/bin/python3


# Move files based on their modify date

import os
import time
import shutil

# Get list of files
dircontent = os.listdir()

# Build dictionary of files as keys and readable mtime as values
metalist = {x: time.strftime("%m/%d/%Y", time.localtime(os.path.getmtime(x)))
            for x in dircontent}


# Build list containing files that were modified on a certain day

files = [m for m in metalist
         if metalist[m] == '03/15/2017' and os.path.isfile(m)]

# Move the files
print('Files to move: {}'.format(' '.join(files)))
choice = ''
while choice.upper() != 'Y' and choice.upper() != 'N':
    print('Press Y to continue or N to exit')
    choice = input().upper()
if choice == 'Y':
    count = 0
    for f in files:
        print('moving ' + f)
        shutil.move(f, './automate_the_boring_stuff')
        count += 1
    print('{} files moved'.format(count))
else:
    print('exiting script')
    exit()
