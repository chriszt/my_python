from matplotlib import pyplot as plt
import numpy as np
import os

x0 = np.array([1, 2])
x1 = np.array([3, 4, 5])
xx, yy = np.meshgrid(x0, x1)
x2 = xx.ravel()
x3 = yy.ravel()
print(len(x2))
print(xx.reshape(6))
print(type(x2))
pass
