import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

w=np.linspace(-4*np.pi,4*np.pi,1000)
E=1
τ=2
plt.ylim(-2,4)
plt.title(u'矩形窗函数的频谱,E=1,τ=2')
fw=2*E*np.sin(w*τ/2)/w
plt.plot(w,fw)
plt.show()
