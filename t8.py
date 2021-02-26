import numpy as np
import pandas as pd
import string

# t = pd.Series(np.arange(10), list(string.ascii_uppercase[:10]))
# print(t)

# t = pd.Series([11, 22, 33, 44], list("abcd"))
# print(t)

# tmp_dict = {"name": "lisi", "age": 18, "tel": 10086}
# print(tmp_dict)
# t = pd.Series(tmp_dict)
# print(t)

# tmp_dict = {"name": ["zhangsan", "lisi"], "age": [18, 20], "tel": [10086, 10010]}
# print(tmp_dict)
# t = pd.Series(tmp_dict)
# print(t)

# t1 = {string.ascii_uppercase[i]: i for i in range(10)}
# print(t1)
# t2 = pd.Series(t1)
# print(t2)
# t3 = pd.Series(t2, list(string.ascii_uppercase[1:10]))
# print(t3)

# t = pd.DataFrame(np.arange(101, 113).reshape(3, 4), list("ABC"), list("WXYZ"))
# print(t)
# print(t.describe())

t = pd.read_csv("./b.csv")
print(t[:2])
print(t["name"])

