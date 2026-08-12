    ##Problem 42 - Damped oscillator

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 20)
y = np.exp(-3.0*t) * np.cos(t)

plt.plot(t, y,
         color = 'purple',
         linestyle = ':',
         linewidth = 2,
         marker = 'o',
         markersize = 1,
         label = 'Damped Oscillator'
)

plt.axhline(0, color = 'black', linewidth = 1)
    # axhline = axix horizontal line
plt.grid(True)
plt.show()
