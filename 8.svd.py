# 특잇값
import numpy as np

mat = np.array([[3,6], [2,3], [0,0], [0,0]])
print(mat)

u, s, vh = np.linalg.svd(mat)
print(u)
print(s)
print(vh)