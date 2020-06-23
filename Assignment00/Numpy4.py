import numpy as np

a = np.arange(1, 10)
b = np.random.randint(1, 10, size=10)


def commonElements(a, b):
    return np.intersect1d(a, b)


print('input array "a" : ', a)
print('input array "b" : ', b)
print('Common Elements are : ', commonElements(a, b))
