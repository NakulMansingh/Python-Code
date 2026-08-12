    ##Problem 40 - sine wave

import numpy as np
import matplotlib.pyplot as plt #Always write as plt

t = np.linspace(0, 2*np.pi, 300)
y = np.sin(t)

plt.plot(t,y) #draw the line
plt.xlabel("time (s)")
plt.ylabel("displacement (m)")
plt.title("Simple Harmonic Motion")
plt.grid(True) #gridlines
plt.show() #show me the graph
