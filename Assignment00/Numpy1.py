import numpy as np
from random import randint

a = np.arange(1, 4)

b = []

for _ in range(3):
    b.append(randint(1, 100))

print('a : ', a)
print('b : ', b)
print('Multiplication', np.multiply(a, b))
print('Dot Product : ', np.dot(a, b))
print('Cross Product : ', np.cross(a, b))
