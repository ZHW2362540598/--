import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def rect_wave(x,c,c0):     #起点为c0，宽度为c的矩形波
     if x>=(c+c0):
          r=0.0
     elif x<c0:
          r=0.0
     else:
          r=1
     return r

t=np.linspace(-4,4,1000)
y=np.array([rect_wave(t,2,-1) for t in t])
plt.ylim(-0.2,1.2)
plt.title(u'矩形窗函数')
plt.plot(t,y)
plt.show()