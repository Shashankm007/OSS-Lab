# Provide an implementation for filter using list comprehensions
def odd(n):
    if n%2:
        return True
    return False

l = [int(i) for i in range(1,6)]

# Filtering odd numbers only
l2 = list(filter(odd, l))
print(l2)