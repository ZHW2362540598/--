import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
t=np.linspace(-3.0,3.0,1000)
plt.ylim(0,4)
f=2*np.exp((complex(-0.5,8))*t)
plt.subplot(221)
plt.title(u'幅度减小的正弦信号')
plt.plot(t,f)
plt.show()
