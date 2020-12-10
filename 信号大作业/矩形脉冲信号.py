import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def Rectangle(t):
    r=np.where(abs(t)<=2,1.0,0.0)
    return r
n=np.arange(-15,16)
plt.ylim(0,2)
plt.title(u'矩形脉冲信号，N1=2')
plt.stem(n,Rectangle(n))
plt.show()