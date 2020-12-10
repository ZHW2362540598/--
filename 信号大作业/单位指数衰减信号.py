import numpy as np
import matplotlib.pyplot as plt

n=np.arange(0,15)
a=3/4
fn=a**n
plt.title(u'x[n]=a**u[n],a=3/4')
plt.stem(n,fn)
plt.show()
