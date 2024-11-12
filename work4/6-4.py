import numpy as np
from scipy.linalg import lu

# 주어진 행렬 A
A = np.array([
    [-1, -1, 0],
    [-1, 2, -1],
    [0, -1, 2]
])

# LU 분해 수행
P, L, U = lu(A)

print("L 행렬:")
print(L)
print("\nU 행렬:")
print(U)

# 첫 번째 경우 b 벡터
b1 = np.array([1, 1, 1])

# Ly = b1를 풀어서 y 계산
y1 = np.linalg.solve(L, b1)

# Ux = y1를 풀어서 x 계산
x1 = np.linalg.solve(U, y1)

print("\n첫 번째 b 벡터에 대한 해 x:")
print(x1)

# 두 번째 경우 b 벡터
b2 = np.array([2, 0, -1])

# Ly = b2를 풀어서 y 계산
y2 = np.linalg.solve(L, b2)

# Ux = y2를 풀어서 x 계산
x2 = np.linalg.solve(U, y2)

print("\n두 번째 b 벡터에 대한 해 x:")
print(x2)
