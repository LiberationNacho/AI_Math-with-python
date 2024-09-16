import numpy as np

def main():
    # 행렬 A와 B 정의
    A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    B = np.array([[1, 2, 2], [3, 4, 5], [3, 7, 6]])

    # 행렬 A와 B의 크기 출력
    A_shape = A.shape
    B_shape = B.shape
    print(f"Shape of matrix A: {A_shape}")
    print(f"Shape of matrix B: {B_shape}")

    # 행렬 A와 B의 덧셈
    A_plus_B = A + B
    print(f"\nA + B:\n{A_plus_B}")

    # 행렬 A와 B의 뺄셈 (A - B) 및 (B - A)
    A_minus_B = A - B
    B_minus_A = B - A
    print(f"\nA - B:\n{A_minus_B}")
    print(f"\nB - A:\n{B_minus_A}")

    # 행렬 A와 B의 곱셈
    A_mul_B = np.dot(A, B)
    print(f"\nA * B:\n{A_mul_B}")

    # 행렬 A의 행렬식
    det_A = np.linalg.det(A)
    print(f"\nDeterminant of matrix A: {int(det_A)}")

    # 행렬 A의 역행렬
    if det_A != 0:
        inv_A = np.linalg.inv(A)
        print(f"\nInverse of matrix A:\n{inv_A}")
    else:
        print("\nMatrix A does not have an inverse.")

main()
