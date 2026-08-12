## Problem 41 - trig fuctions

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 300)
plt.plot(t, np.sin(t), color = 'blue', label = 'sin(t)')
plt.plot(t, np.cos(t), color = 'red', label = 'cos(t)')
plt.plot(t, np.sin(2*t), color = 'green', label = 'sin(2t)', linestyle = '--')

plt.legend()
plt.grid(True)
plt.show()


