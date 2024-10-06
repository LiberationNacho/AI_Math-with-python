import numpy as np

# 문제 a
A = np.array([[8, -2, 0], [2, 0, -2], [2, 0, 2]])
A_inv = np.linalg.matrix_power(A, -1)
print("(a) Inverse matrix of A = \n", A_inv)
print("\n")