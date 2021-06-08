# 3. Write a Python program to remove the nth index character from a nonempty string.

import numpy as np

print("Enter a string: ")
s = np.array(list(input()))
print("Enter index to be removed: ")
ind = int(input())
if ind>=len(s):
    print("index out of range")
else:
    s = np.delete(s, ind)
    result = ""
    for i in s:
        result += i
    print(result)