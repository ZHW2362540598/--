import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

N=500
t = np.linspace(0,12,num=N)
x1 = 5*np.sin(0.5 * math.pi  * t)
plt.subplot(221)
plt.plot(t,x1)
plt.title(u'5sin(pi/2)t')
plt.ylim(-5.0,5.0)

x2 = 5*np.sin(1 * math.pi * t)
plt.subplot(222)
plt.plot(t,x2)
plt.title(u'5sin(pi*t)')
plt.ylim(-5.0,5.0)

x3 = 5*np.sin(1.5 * math.pi  * t)
plt.subplot(212)
plt.plot(t,x3)
plt.title(u'5sin(3pi/2)*t')
plt.ylim(-5.0,5.0)
plt.show()