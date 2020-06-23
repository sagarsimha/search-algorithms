import numpy as np

a = np.random.randint(1, 100, size=(10, 10))
print("The Matrix is ", a)
print('Determinant : ', np.linalg.det(a))
