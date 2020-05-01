# 역행렬
import numpy as np

mat = np.array(range(4)).reshape(2, 2)
print(mat)

mat_inv = np.linalg.inv(mat)
print(mat_inv)

print(np.dot(mat, mat_inv))