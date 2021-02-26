import numpy as np
import pandas as pd
import string

# t = pd.Series(np.arange(10), list(string.ascii_uppercase[:10]))
# print(len(t))

# t = pd.Series([11, 22, 33, 44], list("abcd"))
# print(t)

tmp_dict = {"name": "zhangsan", "age": 18, "tel": 10086}
t = pd.Series(tmp_dict)
print(t.values)

# t1 = {string.ascii_uppercase[i]: i for i in range(10)}
# t2 = pd.Series(t1)
# print(t2['B'])
