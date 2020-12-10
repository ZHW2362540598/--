import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

w=np.linspace(-3*np.pi,3*np.pi,1000)
plt.ylim(-2,6)
plt.title(u'矩形脉冲信号的频谱，N1=2')
fw=(np.sin(2.5*w))/np.sin(w/2)
plt.plot(w,fw)
plt.show()