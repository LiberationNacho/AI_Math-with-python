import numpy as np
# [프로그래밍 실습 6.1]의 LU 분해 함수
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

# LU 분해를 이용하여 Ax=b의 해를 구하는 함수
def LU_Solver(A, b):
    L, U = LU_decomp(A)
    n = len(L)
    # Ly=b 계산
    y = np.zeros((n,1))
    for i in range(0,n):
        y[i] = b[i]
        for k in range(0,i):
            y[i] -= y[k]*L[i,k]
    # Ux=y 계산
    x = np.zeros((n,1))
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        if i < n-1:
            for k in range(i+1,n):
                x[i] -= x[k]*U[i,k]
        x[i] = x[i]/float(U[i,i])
    return x

A = np.array([[1, 2, 1], [2, 3, 3], [-3, -10, 2]])
b = np.array([[2], [1], [0]])

# LU 분해를 이용하여 Ax=b의 해 구하기
x = LU_Solver(A,b)
print("x = \n", x)