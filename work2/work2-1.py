import numpy as np

'''
가우스 조르당 소거법을 수행하는 함수
ranng(n): 0부터 1까지 나열, min(i, j): 숫자 i와 j중 작은 값
abs(i): i의 절댓 값
np.zeros(n): 0으로 이루어진 n차 정방행렬
'''

def Gauss_jordan_Method(A):
    # i번째 열에서 절댓값이 최대인 성분의 행 선택
    (n, m) = A.shape
    A = A.astype(np.float32)

    for i in range( 0, min(n, m)):
        maxEl = abs(A[i, i])
        maxRow_num = i
        for k in range(i + 1, n):
            if abs(A[k. i]) > maxEl:
                maxEl = abs(A[k, i])
                maxRow_num = k

        for k in range(i, m):
            tmp = A[maxRow_num, k]
