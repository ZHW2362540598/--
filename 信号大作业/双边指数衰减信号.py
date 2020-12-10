import numpy as np
import matplotlib.pyplot as plt

n=np.arange(-20,20)
a=0.75
fn=a**abs(n)
plt.title(u'x[n]=a**|n|,a=0.75')
plt.stem(n,fn)
plt.show()
