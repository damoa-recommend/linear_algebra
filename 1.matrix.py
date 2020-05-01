# 행렬생성
import numpy as np

# 행렬
print(np.array([1,2,3,4]))
print(np.array([[1,2,3,4], [11,22,33,44]]))

# 단위행렬(대각성분: 1, 나머지 성분: 0)
mat_4 = np.eye(4)
print(mat_4)

# 영행렬
zero_4 = np.zeros((4, 4))
print(zero_4)

# 대각행렬(diagonal matrix)
x = np.array([[1,2,3], [2,3,4], [4,5,6]])
print(x)
print(np.diag(x))