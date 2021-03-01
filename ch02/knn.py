import numpy as np
import operator as op


def classify(inX, dataSet, labels, k):
    dataSetRows = dataSet.shape[0]
    print("dataSetRows:", dataSetRows)
    diffMat = np.tile(inX, (dataSetRows, 1))
    print("diffMat:\n", diffMat)
    diffMat -= dataSet
    print("diffMat:\n", diffMat)
    sqDiffMat = diffMat ** 2
    print("sqDiffMat:\n", sqDiffMat)
    dists = np.sum(sqDiffMat, 1) ** 0.5
    print("dists:\n", dists)
    sortedIndex = np.argsort(dists)
    print("sortedIndex:\n", sortedIndex)
    clsCount = {}
    for i in range(k):
        iLable = labels[sortedIndex[i]]
        clsCount[iLable] = clsCount.get(iLable, 0) + 1
    print("clsCount:\n", clsCount)
    sortClsCount = sorted(clsCount.items(), key=op.itemgetter(1), reverse=True)
    print("sortClsCount:\n", sortClsCount)
    print("sortClsCount[0][0]:", sortClsCount[0][0])
    return sortClsCount[0][0]


def createDataSet():
    _grp = np.array([[1.0, 1.1],
                     [1.0, 1.0],
                     [0.0, 0.0],
                     [0.0, 0.1]])
    _labs = ["A", "A", "B", "B"]
    print("Group:\n", _grp)
    print("Labels:\n", _labs)
    return _grp, _labs


def file2mat(filename):
    pass

if __name__ == '__main__':
    # group, labels = createDataSet()
    # classify([0.0, 0.0], group, labels, 3)



    # arr1 = np.arange(4).reshape((2, 2))
    # print(np.tile(arr1, (4, 4)))
    pass


