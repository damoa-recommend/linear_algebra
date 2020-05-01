# 대각합
import numpy as np

mat = np.arange(16).reshape(4, 4)
print(mat)
print(np.trace(mat))

mat_3d = np.arange(27).reshape(3, 3, 3)
print(mat_3d)
print(np.trace(mat_3d))