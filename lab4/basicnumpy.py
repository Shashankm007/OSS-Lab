# Basic commands of Numpy

# 1. Import the numpy package under the name np
import numpy as np

# 2. Create a vector with values ranging from 10 to 49.
Z = np.arange(10, 50)
print(Z)

# 3. Reverse a vector
Z = np.arange(50)
Z = Z[::-1]
print(Z)

# 4. Create a 3x3 matrix with values ranging from 0 to 8.
Z = np.arange(9).reshape(3,3)
print(Z)

# 5. Find indices of non-zero elements from [1,2,0,0,4,0]
nz = np.nonzero([1,2,0,0,4,0])
print(nz)

# 6. Create a 3x3 identity matrix
Z = np.eye(3)
print(Z)

# 7. Create a 3x3x3 array with random values
Z = np.random.random((3,3,3))
print(Z)

# 8. Create a 10x10 array with random values and find the minimum and maximum values
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)

# 9. Create a random vector of size 30 and find the mean value
Z = np.random.random(30)
m = Z.mean()
print(m)

# 10. Create a 2d array with 1 on the border and 0 inside.
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)

# 11. How to add a border (filled with 0's) around an existing array?
Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)

# 12. Multiply a 5x3 matrix by a 3x2 matrix
Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)

# 13. Given a 1D array, negate all elements which are between 3 and 8, in place.
Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1
print(Z)

# 14. How to find common values between two arrays?
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(np.intersect1d(Z1,Z2))

# 15. How to get the dates of yesterday, today and tomorrow?
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print(yesterday, today, tomorrow, end="\n")

# 16. How to get all the dates corresponding to the month of July 2016?
Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(Z)

# 17. Consider two random array A and B, check if they are equal

A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
# Assuming identical shape of the arrays and a tolerance for the comparison of values
equal = np.allclose(A,B)
print(equal)
# Checking both the shape and the element values, no tolerance (values have to be exactly equal)
equal = np.array_equal(A,B)
print(equal)

# 18. Create random vector of size 10 and replace the maximum value by 0.
Z = np.random.random(10)
Z[Z.argmax()] = 0
print(Z)
