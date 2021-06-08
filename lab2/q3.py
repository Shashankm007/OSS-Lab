# Write a function group (list, size) that take a list and splits into smaller lists of given size.

def group (list, size):
    groups = []
    for i in range(0, len(list), size):
        groups.append(list[i:min(i+size, len(list))])
    return groups
l = [1,2,3,4,5,6,7,8,9]
size = int(input("Enter size : "))
print(group(l, size))