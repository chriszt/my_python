import numpy as np


# a = np.array([2, np.nan, 10])
# print(a[[True, True, False]])
# print(a[[True, False, False]])

def fill_ndarray(t1):
    for i in range(t1.shape[1]):
        curCol = t1[:, i]
        nanCount = np.count_nonzero(np.isnan(curCol))
        if nanCount != 0:
            notNanCol = curCol[curCol == curCol]
            # print(notNanCol)
            curCol[np.isnan(curCol)] = np.mean(notNanCol)
    return t1


if __name__ == '__main__':
    t = np.arange(24).reshape(4, 6).astype("float")
    print(t)
    print("*" * 20)

    t[1, 2:] = np.nan
    print(t)
    print("*" * 20)

    t = fill_ndarray(t)
    print(t)
