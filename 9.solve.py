# 연립방정식 해 풀기
import numpy as np

mat1 = np.array([[2, -1, 1], [3, 9, -3], [1, 2, -3]])
mat2 = np.array([3, 12, -4])

x = np.linalg.solve(mat1, mat2)
print(mat1)
print(mat2)
print(x)

# 검산
print(np.allclose(np.dot(mat1, x), mat2))