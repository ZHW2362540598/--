import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def dwxl(t):
    r=np.where(t==0.0,1.0,0.0)
    return r
n=np.arange(-4,5)
plt.ylim(0,2)
plt.title(u'单位脉冲信号')
plt.stem(n,dwxl(n))
plt.show()