import numpy as np
import matplotlib.pyplot as plt

w=np.linspace(-5,5)
a=1j
plt.ylim(0,2)
plt.title(u"1/(1+jw)")
fw=1/(1+w*a)
plt.plot(w,fw)
plt.show()