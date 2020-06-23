import numpy as np

a = np.arange(1, 30)


def negativeEven(inpArr):
    return [-1 * i if i % 2 == 0 else i for i in inpArr]


print('input array : ', a)
print('Negative Even Numbers : ', negativeEven(a))
