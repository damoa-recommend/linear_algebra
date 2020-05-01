# 고유값
import numpy as np

mat = np.array([[4, 2], [3, 5]])
print(mat)

w, v = np.linalg.eig(mat)
print(w)
print(v)