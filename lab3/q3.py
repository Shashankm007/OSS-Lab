# Provide an implementation for map using list comprehensions.
def square(n):
    return n*n

l = [str[i] for i in range(1, 6)]

#converting each element from string to integer
l2 = list(map(int, l))

#squaring each element of list
l2 = list(map(square, l2))
print(l2)