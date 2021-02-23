import random
from matplotlib import pyplot as plt
# from matplotlib import rc
from matplotlib import font_manager

# font = {'family': 'Microsoft YaHei'}
# rc('font', **font)

# rc('font', family='Microsoft YaHei')

x = range(120)
y = [random.randint(20, 35) for i in x]

my_font = font_manager.FontProperties(fname="/usr/share/fonts/truetype/win10-fonts/msyh.ttc")
print(my_font)

plt.plot(x, y)

_labels = ["10点%02d分" % i for i in range(60)]
_labels += ["11点%02d分" % i for i in range(60)]
print(_labels)
plt.xticks(x[::5], _labels[::5], rotation=45, fontproperties=my_font)

plt.show()
