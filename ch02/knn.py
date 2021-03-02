from matplotlib import pyplot as plt
import numpy as np
import operator as op


def classify(inX, ds, dsLabs, k):
    dataSetSize = ds.shape[0]
    # print("dataSetRows:", dataSetSize)
    diffMat = np.tile(inX, (dataSetSize, 1))
    diffMat -= ds
    sqDiffMat = diffMat ** 2
    dists = np.sum(sqDiffMat, 1) ** 0.5
    # print("dists:\n", dists)
    sortedIndex = np.argsort(dists)
    # print("sortedIndex:\n", sortedIndex)
    clsCount = {}
    for i in range(k):
        sortedLabels = dsLabs[sortedIndex[i]]
        clsCount[sortedLabels] = clsCount.get(sortedLabels, 0) + 1
    # print("clsCount:\n", clsCount)
    clsCountItems = clsCount.items()
    # print("clsCountItems:\n", clsCountItems)
    sortedClsCount = sorted(clsCountItems, key=op.itemgetter(1), reverse=True)
    # print("sortedClsCount:\n", sortedClsCount)
    # print("sortedClsCount[0][0]:\n", sortedClsCount[0][0])
    return sortedClsCount[0][0]
2

def createDataSet():
    _grp = np.array([[1.0, 1.1],
                     [1.0, 1.0],
                     [0.0, 0.0],
                     [0.0, 0.1]])
    _labs = ["A", "A", "B", "B"]
    # print("Group:\n", _grp)
    # print("Labels:\n", _labs)
    return _grp, _labs


def file2mat(filename):
    # fp = open(filename)
    with open(filename) as fp:
        dataLst = fp.readlines()
        # print("dataLst:\n", dataLst)
        nRows = len(dataLst)
        # print("nRows:", nRows)
        retMat = np.zeros((nRows, 3))
        # print("retMat:\n", retMat)
        clsLabVec = []
        idx = 0
        for curLine in dataLst:
            curLine = curLine.strip()
            # print(curLine)
            curLst = curLine.split('\t')
            # print(curLst)
            retMat[idx, :] = curLst[0:3]
            clsLabVec.append(int(curLst[-1]))
            idx += 1
        # print(retMat)
        # print(clsLabVec)
        return retMat, clsLabVec


if __name__ == '__main__':
    ########## Test 1 ##########
    # group, labels = createDataSet()
    # tp = [0.0, 0.0]
    # tpCls = classify(tp, group, labels, 3)
    # print("{0} --> {1}".format(tp, tpCls))

    ########## Test 2 ##########
    # file2mat("/dev/random")
    datDataMat, datLabels = file2mat("./datingTestSet2.txt")
    # print("datDataMat:\n", datDataMat)
    # print("datLabels:\n", datLabels)
    print(datDataMat[1:3, 1], datDataMat[1:3, 2])
    plt.scatter(datDataMat[1:3, 1], datDataMat[1:3, 2])
    plt.scatter(datDataMat[3:5, 1], datDataMat[3:5, 2])

    plt.grid()
    plt.show()


    ########## Test X ##########
    # arr1 = np.arange(4).reshape((2, 2))
    # print(arr1)
    # # arr1 = np.tile(arr1, 2)
    # print(np.tile(arr1, 2))
    # # arr1 = np.tile(arr1, (1, 2))
    # print(np.tile(arr1, (1, 2)))

    # fruits = {"apple": 3, "banana": 2, "pear": 5, "orange": 1}
    # print(fruits)
    # items = fruits.items()
    # print(items)
    # items = sorted(items, key=op.itemgetter(1), reverse=True)
    # print(items)
    # for i in items:
    #     print(i[1])

    # t = np.arange(12).reshape(3, 4)
    # print(t)
    # t[1, :] = np.arange(1, 5)
    # print(t)
    pass
