import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn import neighbors
from sklearn import model_selection


def test1():
    X, y = datasets.make_blobs(200, n_features=2, centers=2, random_state=8)
    # print(x[:, 0], x[:, 1])
    # print(plt.cm.get_cmap("spring"))
    # print(plt.cm.spring)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.get_cmap("spring"), edgecolors='k')
    plt.plot()
    plt.grid()
    plt.show()


def test2():
    # X = [[0], [1], [2], [3]]
    # y = [0, 0, 1, 1]
    # print(X)
    # print(y)
    # clf = neighbors.KNeighborsClassifier(3)
    # clf.fit(X, y)
    # clsRet = clf.predict([[1.6]])
    # print(clsRet)

    X, y = datasets.make_blobs(200, centers=2)
    testData = [6.75, 4.82]

    clf = neighbors.KNeighborsClassifier()
    clf.fit(X, y)

    X0_min = X[:, 0].min() - 1
    X0_max = X[:, 0].max() + 1
    X1_min = X[:, 1].min() - 1
    X1_max = X[:, 1].max() + 1
    t0 = np.arange(X0_min, X0_max, 0.02)
    t1 = np.arange(X1_min, X1_max, 0.02)
    xx, yy = np.meshgrid(t0, t1)
    t2 = xx.ravel()
    t3 = yy.ravel()
    t4 = np.c_[t2, t3]
    t5 = clf.predict(t4)
    testDataRes = clf.predict(np.array(testData).reshape(1, 2))
    print(testDataRes)
    t6 = t5.reshape(xx.shape)
    plt.pcolormesh(xx, yy, t6, cmap=plt.cm.Pastel1)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.spring, edgecolors='k')
    plt.scatter(testData[0], testData[1], 200, 'r', '*')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("Classifier: KNN")
    plt.show()
    pass


def test3():
    X, y = datasets.make_blobs(500, centers=5)

    clf = neighbors.KNeighborsClassifier()
    clf.fit(X, y)

    X0_min = X[:, 0].min() - 1
    X0_max = X[:, 0].max() + 1
    X1_min = X[:, 1].min() - 1
    X1_max = X[:, 1].max() + 1
    t0 = np.arange(X0_min, X0_max, 0.02)
    t1 = np.arange(X1_min, X1_max, 0.02)
    xx, yy = np.meshgrid(t0, t1)
    t2 = xx.ravel()
    t3 = yy.ravel()
    t4 = np.c_[t2, t3]
    Z = clf.predict(t4)
    Z = Z.reshape(xx.shape)
    print("score=", clf.score(X, y))

    plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Pastel1)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.spring, edgecolors='k')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("Classifier: KNN")
    plt.show()


def test4():

    pass


if __name__ == "__main__":
    ########## Test 1 ##########
    # test1()

    ########## Test 2 ##########
    test2()

    ########## Test 3 ##########
    # test3()

    ########## Test 4 ##########
    # test4()

    pass
