import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,10)
plt.ylim(0,2)
plt.title(u'e(-t)u(t)')
ft=np.exp(-t)
plt.plot(t,ft)
plt.show()
