import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

w=np.linspace(-3*np.pi,3*np.pi,1000)
plt.ylim(0,8)
plt.title(u'双边指数衰减信号的频谱，a=0.75')
fw=(1-0.75*0.75)/(1-2*0.75*np.cos(w)+0.75*0.75)
plt.plot(w,fw)
plt.show()
