import numpy as np

# LU 분해 함수
def LU_decomp(A):
    (n,m) = A.shape
    L = np.zeros((n,n)) # 빈 행렬 L 만들기
    U = np.zeros((n,n)) # 빈 행렬 U 만들기
    # 행렬 L과 U 계산
    for i in range(0, n):
        for j in range(i, n):
            U[i, j] = A[i, j]
            for k in range(0, i):
                U[i, j] = U[i, j] - L[i, k]*U[k, j]
        L[i,i] = 1
        if i < n-1:
            p = i + 1
            for j in range(0,p):
                L[p, j] = A[p, j]
                for k in range(0, j):
                    L[p, j] = L[p, j] - L[p, k]*U[k, j]
                    L[p,j] = L[p,j]/U[j,j]
    return L, U

A = np.array([[1, 2, 1], [2, 3, 3], [-3, -10, 2]])

# 행렬 A의 LU 분해
L, U = LU_decomp(A)

print("A = \n", A)
print("\n")
print("L = \n", L)
print("\n")
print("U = \n", U)
print("\n")