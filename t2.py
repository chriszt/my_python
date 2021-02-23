from matplotlib import pyplot as plt
# from matplotlib import font_manager
from matplotlib import rc

# zh_font = font_manager.FontProperties(fname="/usr/share/fonts/truetype/win10-fonts/msyhl.ttc")
zh_font = {"family": "Microsoft YaHei"}
rc("font", **zh_font)

x = range(20)
x_labels = ["%d岁" % i for i in range(11, 31)]

a = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
b = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# print("x:\n", list(x))
# print("x_labels:\n", x_labels)

plt.plot(x, a, label="自己")
plt.plot(x, b, label="同桌")

# plt.xticks(x, x_labels, fontproperties=zh_font, rotation=45)
# plt.legend(prop=zh_font, loc="center")
plt.xticks(x, x_labels, rotation=45)
plt.legend(loc="upper left")

plt.show()

