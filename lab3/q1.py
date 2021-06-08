# Write a program to count frequency of characters in a paragraph.

from collections import defaultdict

def charFreq(s):
    s = s.lower()
    d = defaultdict(int)
    for i in s:
        d[i] += 1
    for key, val in d.items():
        print("{}: {} times".format(key, val))
charFreq("I am Shashank studying in JIIT") 