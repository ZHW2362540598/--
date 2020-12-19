import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(-10,10,1000)
plt.ylim(0,2)
plt.title(u"e(-|t|)")
ft=np.exp(-abs(t))
plt.plot(t,ft)
plt.show()