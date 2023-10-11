np.array([1, 2, 7.9, 11.1], dtype=np.int64)

a = np.array([1, 2, 3, 4], dtype=np.uint8)



m1 = [
    [4, 0, 0],
    [0, 4, 0],
    [0, 0, 4]
]


m2 = np.array(m2, dtype=np.int16)

m3 = np.zeros((4, 3), dtype=np.uint8)

m4 = np.ones((10, 2), dtype=float)

m5 = np.eye(5)
m5


import math

x_coords = np.linspace(-2 * math.pi, 2 * math.pi, 50)
x_coords

y_values = np.array([math.sin(x) for x in x_coords])
y_values


import numpy as np 
mat1 = np.arange(12)
mat1

mat2 = mat1.reshape(4,3)
mat2.shape

mat3 = mat1.reshape(3,4).copy() # Creates a new copy of the matrix

mat4 = np.array([[1,2,3],[4,5,6]])
mat4.shape



When vertical stacking is performed each array must have the same number of columns.

When horizontal stacking is performed, each array must have the same number of rows.

import numpy as np

b1 = np.arange(11, 16)
b1

c2 = np.arange(11, 21).reshape(2, 5)
c2

d1 = np.vstack((b1, c2))
d1



Vector Operations
import numpy as np

# define vector
v = np.array([1, 2, 3])
print(f"v: {v}")

Vector Addition:
----------------
a = np.array([1, 2, 3])
print(f"a = {a}\n")

b = np.array([1, 2, 3])
print(f"b = {b}\n")

c = a + b
print(f"c = {c}\n")


Vector Subtraction:
----------------------
b = np.array([0.5, 0.5, 0.5])
print(f"b = {b}\n")

c = a - b
print(f"c = {c}")


Vector Multiplication:
----------------------
a = np.array([1, 2, 3])
print(f"a = {a}\n")

b = np.array([1, 2, 3])
print(f"b = {b}\n")


c = a * b
print(f"c = {c}\n")


Vector Division:
----------------
c = a / b
print(f"c = {c}")


Vector Dot Product:
------------------
c = a.dot(b)
print(f"c = {c}")

Vector Scalar Multiplication:
-----------------------------
a = np.array([2, 4, 6])
print(f"a = {a}\n")

s = 0.5
print(f"scalar s = {s}\n")

c = s * a
print(f"c = {c}")


Vector L1 Norm:
-------------
from numpy import array, inf
from numpy.linalg import norm



a = array([1, 2, 3])
print(f"a = {a}\n")

l1 = norm(a, 1)
print(f"l1 = {l1}")



Vector L2 Norm:
---------------

Vector L2 Norm:

Also known as Euclidean norm

l2 = norm(a)
print(f"l2 = {l2}")

