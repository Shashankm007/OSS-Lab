# Write a program reverse.py to print lines of a file in reverse order.

f = open("file.txt", 'r')
lines = f.readlines()

for line in range(-1, -len(lines)-1, -1):
    print(lines[line].rstrip('\n'))