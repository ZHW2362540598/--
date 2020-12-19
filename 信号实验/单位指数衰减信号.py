import numpy as np
import matplotlib.pyplot as plt

n=np.arange(0,15)
a=0.75
fn=a**n
plt.title(u'x[n]=a**nu[n],a=0.75')
plt.stem(n,fn)
plt.show()
