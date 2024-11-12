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

print("(a) A^T A:\n", A_a_TA)
print("(a) A^T A의 고유값:", eigenvalues_A_a_TA)
print("(a) AA^T:\n", A_a_AT)
print("(a) AA^T의 고유값:", eigenvalues_A_a_AT)

# (b) A 행렬
A_b = np.array([
    [3, 0],
    [2, 0]
])

# (b) A^T A와 AA^T 계산
A_b_TA = A_b.T @ A_b
A_b_AT = A_b @ A_b.T

# (b) 각 행렬의 고유값 계산
eigenvalues_A_b_TA = np.linalg.eigvals(A_b_TA)
eigenvalues_A_b_AT = np.linalg.eigvals(A_b_AT)

print("\n(b) A^T A:\n", A_b_TA)
print("(b) A^T A의 고유값:", eigenvalues_A_b_TA)
print("(b) AA^T:\n", A_b_AT)
print("(b) AA^T의 고유값:", eigenvalues_A_b_AT)
