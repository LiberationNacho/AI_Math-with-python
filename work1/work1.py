import numpy as np

# 행렬 A와 B 정의
A = np.array([[4, 7], [2, 6]])
B = np.array([[3, 8], [5, 1]])

# 1) 행렬 A와 B의 크기 출력
A_shape = A.shape
B_shape = B.shape
print(f"행렬 A의 크기: {A_shape}")
print(f"행렬 B의 크기: {B_shape}")

# 2) 행렬 A와 B의 덧셈
A_plus_B = A + B
print(f"\nA + B:\n{A_plus_B}")

# 3) 행렬 A와 B의 뺄셈 (A - B) 및 (B - A)
A_minus_B = A - B
B_minus_A = B - A
print(f"\nA - B:\n{A_minus_B}")
print(f"\nB - A:\n{B_minus_A}")

# 4) 행렬 A와 B의 곱셈
A_mul_B = np.dot(A, B)
print(f"\nA * B:\n{A_mul_B}")

# 5) 행렬 A의 행렬식
det_A = np.linalg.det(A)
print(f"\n행렬 A의 행렬식: {det_A}")

# 6) 행렬 A의 역행렬
if det_A != 0:
    inv_A = np.linalg.inv(A)
    print(f"\n행렬 A의 역행렬:\n{inv_A}")
else:
    print("\n행렬 A는 역행렬이 없습니다.")
