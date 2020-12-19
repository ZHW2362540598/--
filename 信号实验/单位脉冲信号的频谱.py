import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

w=np.linspace(-5,5)
plt.ylim(0,2)
plt.title(u'单位脉冲信号的频谱')
fw=(1/w)*w
plt.plot(w,fw)
plt.show()