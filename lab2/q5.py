# Write a function extsort to sort a list of files based on extension.

import os

def extsort(files):
    files.sort(key=lambda x: os.path.splitext(x)[1])

l = ['a.c', 'b.py', 'readme.md', 'file.txt', 'x.cpp']
extsort(l)
print(l)