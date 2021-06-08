# Write a function “duplicate” to find all duplicates in the list.

def duplicate(l):
    l2 = []
    duplicates = []
    for i in l:
        if i in l2:
            duplicates.append(i)
        else:
            l2.append(i)
    return duplicates
l = [1,2,3,3,4,5,6,6,7,7,45,45,56]
print(duplicate(l))