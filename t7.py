import numpy as np

t1 = np.arange(12).reshape(2, 6)
print("t1:\n", t1)

t2 = np.arange(12, 24).reshape(2, 6)
print("t2:\n", t2)

t3 = np.vstack((t1, t2))
print("t3:\n", t3)

t4 = np.hstack((t1, t2))
print("t4:\n", t4)
