# 선형대수 함수

* 단위행렬(Unit matrix): np.eye(n)
* 영행렬(Zero matrix): np.zeros(n)
* 대각행렬(Diagonal matrix): np.diag(x)
* 내적(Dot product, inner product): np.dot(a, b)
* 전치행렬(Transpose Matrix): np.T, np.transpose(a)
* 대각합(trace): np.trace(x)
* 행렬식(Matrix Determinant): np.linalg.det(x)
* 역행렬(Inverse of a matrix): np.linalg.inv(x)
* 고유값(Eigenvalue), 고유백터(Eigenvector): w, v = np.linalg.eig(x)
* 특잇값 분해(Singular Value Decomposition): u, s, vh = np.linalg.svd(A)
* 연립방정식 해 풀기: np.linalg.solve(a, b)
* 최소제곱법: m, c = np.linalg.lstsq(A, y, rcond=None)