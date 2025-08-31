import numpy as np

# np.linalg.inv() – Matrix Inverse

A = np.array([[1, 2],
              [3, 4]])

A_inv = np.linalg.inv(A)
print("Inverse:\n", A_inv)

print(np.dot(A, A_inv))

# np.linalg.det() – Determinant

A = np.array([[2, 3],
              [1, 4]])

det_A = np.linalg.det(A)
print("Determinant:", det_A)

# 3. np.linalg.eig() – Eigenvalues & Eigenvectors

A = np.array([[2, 0],
              [0, 3]])

values, vectors = np.linalg.eig(A)
print("Eigenvalues:", values)
print("Eigenvectors:\n", vectors)

# 4. np.linalg.solve() – Solving Linear Equations

A = np.array([[2, 1],
              [3, 4]])
b = np.array([8, 18])

x = np.linalg.solve(A, b)
print("Solution [x, y]:", x)
