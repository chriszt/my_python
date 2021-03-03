import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn import neighbors
from sklearn import model_selection


def test1():
    x, y = datasets.make_blobs(200, n_features=2, centers=2, random_state=8)
    # print(x[:, 0], x[:, 1])
    # print(plt.cm.get_cmap("spring"))
    # print(plt.cm.spring)
    plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.get_cmap("spring"), edgecolors='k')
    plt.grid()
    plt.show()


def test2():
    pass


if __name__ == "__main__":
    ########## Test 1 ##########
    # test1()

    ########## Test 1 ##########
    test2()

    pass
