import numpy as np
import operator as op


a = [1, 2, 3]
b = [3, 4, 5]
x = op.lt(a, b)
print(x.__index__())
print(op.index(x))
