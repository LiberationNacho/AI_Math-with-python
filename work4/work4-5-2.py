import numpy as np
import sympy as sp

# 행렬 A의 케일리-해밀턴 정리 만족 여부 확인
print("문제 (a)")
A = sp.Matrix([[1, -4, 1], [3, 2, 3], [1, 1, 3]])
print("A = ", A)
lamda = sp.symbols('lamda')
p_A = A.charpoly(lamda)
print("A의 특성다항식 : ",p_A)
print("특성다항식의 영이 아닌 계수들 : ", p_A.coeffs())

# 행렬 A의 특성다항식을 먼저 구한 후 직접 행렬다항식을 코드로 작성하는 방법
A2 = np.matmul(A, A)
A3 = np.matmul(A, A2)
char_coeff = p_A.coeffs()
print("p_A(A) = ",char_coeff[0]*A3 + char_coeff[1]*A2 + char_coeff[2]*A + char_coeff[3]*np.eye(3))
print("\n")

# 행렬 B의 케일리-해밀턴 정리 만족 여부 확인
print("문제 (b)")
B = sp.Matrix([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]])
print("B = ", B)
lamda = sp.symbols('lamda')
p_B = B.charpoly(lamda)
print("B의 특성다항식 : ", p_B)
print("특성다항식의 영이 아닌 계수들 : ", p_B.coeffs())

# 행렬 B의 특성다항식을 먼저 구한 후 직접 행렬다항식을 코드로 작성하는 방법
B2 = np.matmul(B, B)
B3 = np.matmul(B, B2)
B4 = np.matmul(B, B3)
char_coeff = p_B.coeffs()
print("p_B(B) = \n", char_coeff[0]*B4 + char_coeff[1]*B2 )
print("\n")

# 행렬 C의 케일리-해밀턴 정리 만족 여부 확인
print("문제 (c)")
C = sp.Matrix([[2, -1, 0, -1], [-1, 2, -1, 0], [0, -1, 2, -1], [-1, 0, -1, 2]])
print("C = ", C)
lamda = sp.symbols('lamda')
p_C = C.charpoly(lamda)
print("C의 특성다항식 : ", p_C)
print("특성다항식의 영이 아닌 계수들 : ", p_C.coeffs())

# 행렬 C의 특성다항식을 먼저 구한 후 직접 행렬다항식을 코드로 작성하는 방법
C2 = np.matmul(C, C)
C3 = np.matmul(C, C2)
C4 = np.matmul(C, C3)
char_coeff = p_C.coeffs()
print("p_C(C) = ",char_coeff[0]*C4 + char_coeff[1]*C3 +char_coeff[2]*C2 + char_coeff[3]*C)