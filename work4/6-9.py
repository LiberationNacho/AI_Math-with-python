import numpy as np

# (a) A 행렬
A_a = np.array([
    [1, 0],
    [1, 1],
    [-1, 1]
])

# (a) A^T A와 AA^T 계산
A_a_TA = A_a.T @ A_a
A_a_AT = A_a @ A_a.T

# (a) 각 행렬의 고유값 계산
eigenvalues_A_a_TA = np.linalg.eigvals(A_a_TA)
eigenvalues_A_a_AT = np.linalg.eigvals(A_a_AT)

# (a) A^T A와 AA^T의 특잇값 분해
U_a_TA, S_a_TA, Vt_a_TA = np.linalg.svd(A_a_TA)
U_a_AT, S_a_AT, Vt_a_AT = np.linalg.svd(A_a_AT)

print("(a) A^T A의 특잇값 분해:")
print("U_a_TA:\n", U_a_TA)
print("S_a_TA (특잇값):", S_a_TA)
print("Vt_a_TA:\n", Vt_a_TA)

print("(a) AA^T의 특잇값 분해:")
print("U_a_AT:\n", U_a_AT)
print("S_a_AT (특잇값):", S_a_AT)
print("Vt_a_AT:\n", Vt_a_AT)

print("(a) A^T A:\n", A_a_TA)
print("(a) A^T A의 고유값:", eigenvalues_A_a_TA)
print("(a) AA^T:\n", A_a_AT)
print("(a) AA^T의 고유값:", eigenvalues_A_a_AT)

# (b) A 행렬
A_b = np.array([
    [3, 0, 2],
    [2, 0, 0]
])

# (b) A^T A와 AA^T 계산
A_b_TA = A_b.T @ A_b
A_b_AT = A_b @ A_b.T

# (b) 각 행렬의 고유값 계산
eigenvalues_A_b_TA = np.linalg.eigvals(A_b_TA)
eigenvalues_A_b_AT = np.linalg.eigvals(A_b_AT)

# (b) A^T A와 AA^T의 특잇값 분해
U_b_TA, S_b_TA, Vt_b_TA = np.linalg.svd(A_b_TA)
U_b_AT, S_b_AT, Vt_b_AT = np.linalg.svd(A_b_AT)

print("\n(b) A^T A의 특잇값 분해:")
print("U_b_TA:\n", U_b_TA)
print("S_b_TA (특잇값):", S_b_TA)
print("Vt_b_TA:\n", Vt_b_TA)

print("(b) AA^T의 특잇값 분해:")
print("U_b_AT:\n", U_b_AT)
print("S_b_AT (특잇값):", S_b_AT)
print("Vt_b_AT:\n", Vt_b_AT)

print("\n(b) A^T A:\n", A_b_TA)
print("(b) A^T A의 고유값:", eigenvalues_A_b_TA)
print("(b) AA^T:\n", A_b_AT)
print("(b) AA^T의 고유값:", eigenvalues_A_b_AT)
