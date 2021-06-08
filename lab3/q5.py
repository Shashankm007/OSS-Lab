# Write a function triplets that takes a number ‘n’ as argument and returns a list of triplets
# such that sum of first two elements of the triplet equals the third element using
# numbers below n. Please note that (a,b, c) and (b, a, c) represent same triplet.

def triplets(n):
    l = []
    for i in range(2, n):
        for j in range(1, i//2+1):
            l.append((j, i-j, i))
    return l

n = int(input())
print(triplets(n))