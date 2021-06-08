# Write a function “lensort” to sort a list of strings based on length.

def lensort(l):
    l.sort(key=len)

l = ['keshav', 'assignment', 'aaaa', 'hello' ]
lensort(l)
print(l)