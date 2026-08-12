    ##Problem 43 - subplots

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4*np.pi, 300)
fig,(ax1, ax2) = plt.subplots(2, 1, figsize=(8,5))
        #where it should be and how it should be
        # 2 rows, 1 column of panel

ax1.plot(t, np.sin(t), color = 'blue')
ax1.set_ylabel("Postion x(t)")
ax1.set_xlabel("time (s)")
ax1.set_title("Postion & Velocity")
ax1.grid()

ax2.plot(t, np.cos(t), color = 'red')
ax2.set_ylabel("Velocity v(t)")
ax2.set_xlabel("time (s)")
ax2.grid()

plt.tight_layout()
plt.show()
