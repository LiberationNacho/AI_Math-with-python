import numpy as np

# (a) L(x, y) = (3x, 4y)
L_a = np.array([[3, 0], [0, 4]])
print("(a) 표준행렬:\n", L_a)

# (b) L(x, y) = (x + y, y, x)
L_b = np.array([[1, 1], [0, 1], [1, 0]])
print("(b) 표준행렬:\n", L_b)

# (c) L(x, y, z) = (x + z, y)
L_c = np.array([[1, 0, 1], [0, 1, 0]])
print("(c) 표준행렬:\n", L_c)
