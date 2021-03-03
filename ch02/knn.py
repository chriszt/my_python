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


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    deltas = maxVals - minVals
    normDataSet = np.zeros(dataSet.shape)
    rowNum = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (rowNum, 1))
    normDataSet = normDataSet / np.tile(deltas, (rowNum, 1))
    return normDataSet, deltas, minVals


def createDataSet():
    _grp = np.array([[1.0, 1.1],
                     [1.0, 1.0],
                     [0.0, 0.0],
                     [0.0, 0.1]])
    _labs = ["A", "A", "B", "B"]
    # print("Group:\n", _grp)
    # print("Labels:\n", _labs)
    return _grp, _labs


def datClsTest():
    sepRation = 0.1
    datDataMat, datLabels = file2mat("./datingTestSet2.txt")
    normMat, deltas, minVals = autoNorm(datDataMat)
    rowNum = normMat.shape[0]
    testVecNum = int(rowNum * sepRation)
    errCount = 0.0
    for i in range(testVecNum):
        clsRes = classify(normMat[i, :], normMat[testVecNum:rowNum, :], datLabels[testVecNum:rowNum], 3)
        print("The classifier came back with: %d, the real answer is: %d" % (clsRes, datLabels[i]))
        if clsRes != datLabels[i]:
            errCount += 1.0
    print("the total error rate is: %f" % (errCount / float(testVecNum)))
    print(errCount)


def clsPerson():
    resLabels = ["Not at all", "Small doses", " Large doses"]
    mile = float(input("frequent flier miles earned per year: "))
    game = float(input("percentage of time spent playing video games: "))
    ice = float(input("liters of ice cream consumed per year: "))
    datDataMat, datLabels = file2mat("./datingTestSet2.txt")
    normMat, deltas, minVals = autoNorm(datDataMat)
    newArr = np.array([mile, game, ice])
    # print(newArr)
    newArrNorm = (newArr - minVals) / deltas
    # print(newArrNorm)
    clsRes = classify(newArrNorm, datDataMat, datLabels, 3)
    print("You will probably like this person: ", resLabels[clsRes - 1])


def img2Vec(filename):
    retVec = np.zeros((1, 1024))
    with open(filename) as fp:
        for i in range(32):
            curLine = fp.readline().strip()
            # print(curLine)
            for j in range(32):
                retVec[0, (i * 32) + j] = curLine[j]
    return retVec


def handWriteTest():
    hwLables = []

    pass


if __name__ == '__main__':
    ########## Test 1 ##########
    # group, labels = createDataSet()
    # tp = [0.0, 0.0]
    # tpCls = classify(tp, group, labels, 3)
    # print("{0} --> {1}".format(tp, tpCls))

    ########## Test 2 ##########
    # file2mat("/dev/random")
    # datDataMat, datLabels = file2mat("./datingTestSet2.txt")
    # normMat, deltas, minVals = autoNorm(datDataMat)
    # print("datDataMat:\n", datDataMat)
    # print("datLabels:\n", datLabels)
    # print(datDataMat[:, 1], datDataMat[:, 2])
    # print(np.array(datLabels))
    # plt.scatter(datDataMat[:, 1], datDataMat[:, 2], 6 ** 2)
    # print(plt.rcParams["lines.markersize"])
    # plt.scatter(datDataMat[:, 1], datDataMat[:, 2], datLabels)
    # plt.grid()
    # plt.show()

    ########## Test 3 ##########
    # datClsTest()

    ########## Test 4 ##########
    # clsPerson()

    ########## Test 5 ##########
    # img2Vec("trainingDigits/0_0.txt")

    ########## Test 6 ##########
    handWriteTest()

    ########## Test X ##########
    # t0 = np.arange(4).reshape((2, 2))
    # print(t0)
    # t1 = np.tile(t0, 2)
    # print(t1)
    # t2 = np.tile(t0, (1, 2))
    # print(t2)
    # t3 = np.tile(t0, (2, 1))
    # print(t3)
    # t4 = np.tile(t0, (2, 2))
    # print(t4)

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
