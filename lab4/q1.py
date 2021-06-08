# 1. Using numpy, WAP that takes an input from the user in the form of a list and calculate the
# frequency of occurrence of each character/integer in that list (count the number of
# characters).

import numpy as np

print("Enter elements of the list space separated: ")
ini_array = np.array(input().split())

unique, frequency = np.unique(ini_array, return_counts=True)
for x, y in zip(unique, frequency):
    print("{} appeared {} times".format(x,y))
