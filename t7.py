import numpy as np

# t1 = np.arange(12, dtype="float").reshape(3, 4)
# print(t1)
#
# t2 = np.zeros((3, 4), dtype="bool")
# t2[0, 1] = True
# t2[1, 0] = True
# t2[1, 2] = True
# print(t2)
#
# t3 = t1 * t2
# print(t3)

t1 = np.arange(1, 13).reshape(3, 4)
print("t1:\n", t1)

t2 = np.array([[True, False, False, False],
               [True, True, False, False],
               [False, False, False, True]])
print("t2:\n", t2)

t3 = t1[t2]
print("t3:\n", t3)

