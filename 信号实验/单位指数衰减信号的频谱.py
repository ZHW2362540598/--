import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

w=np.linspace(-2*np.pi,2*np.pi,1000)
plt.ylim(0,5)
plt.title(u'单位指数衰减信号的频谱，a=0.75')
a=1j
fw=1/(1-0.75*np.exp(-a*w))
plt.plot(w,fw)
plt.show()
