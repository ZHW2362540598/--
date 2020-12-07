import numpy as np
import matplotlib.pyplot as plt

w=np.linspace(-5,5)
plt.ylim(0,2)
plt.title(u"2/(1+w^2)")
fw=2/(1+w*w)
plt.plot(w,fw)
plt.show()