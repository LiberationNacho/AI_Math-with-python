import numpy as np

# 행렬 A의 특잇값 분해
A = np.array([[6, 4], [0,0], [4,0]])
print("A = \n", A)
print("\n")

U, Sig, VT = np.linalg.svd(A) # 특잇값 분해
print("U= \n", U)
print("\n")

m, n = A.shape
Sigma = np.zeros((m, n)) # m×n 행렬 Σ
k = np.size(Sig)
Sigma[:k, :k] = np.diag(Sig) # 특잇값
print("Sigma = \n", Sigma)
print("\n")
print("V^T = \n", VT) # n×n 행렬 V^T
print("\n")

# 행렬 B 의 특잇값 분해
B = np.array([[1, 1, -1], [0,1,1]])
print("B = \n", B)
print("\n")

U, Sig, VT = np.linalg.svd(B) # 특잇값 분해
print("U= \n", U)
print("\n")

m, n = B.shape
Sigma = np.zeros((m, n)) # m×n 행렬 Σ
k = np.size(Sig)
Sigma[:k, :k] = np.diag(Sig) # 특잇값
print("Sigma = \n", Sigma)
print("\n")
print("V^T = \n", VT) # n×n 행렬 V^T
print("\n")