import numpy as np

# (a) L(x, y) = (3x, 4y)
L_a = np.array([[3, 0], [0, 4]])
print("(a) 표준행렬:\n", L_a)

# 특잇값 분해
U_a, S_a, Vt_a = np.linalg.svd(L_a)
print("(a) 특잇값 분해 결과:")
print("U_a:\n", U_a)
print("S_a:\n", S_a)
print("Vt_a:\n", Vt_a)

# (b) L(x, y) = (x + y, y, x)
L_b = np.array([[1, 1], [0, 1], [1, 0]])
print("\n(b) 표준행렬:\n", L_b)

# 특잇값 분해
U_b, S_b, Vt_b = np.linalg.svd(L_b)
print("(b) 특잇값 분해 결과:")
print("U_b:\n", U_b)
print("S_b:\n", S_b)
print("Vt_b:\n", Vt_b)

# (c) L(x, y, z) = (x + z, y)
L_c = np.array([[1, 0, 1], [0, 1, 0]])
print("\n(c) 표준행렬:\n", L_c)

# 특잇값 분해
U_c, S_c, Vt_c = np.linalg.svd(L_c)
print("(c) 특잇값 분해 결과:")
print("U_c:\n", U_c)
print("S_c:\n", S_c)
print("Vt_c:\n", Vt_c)
