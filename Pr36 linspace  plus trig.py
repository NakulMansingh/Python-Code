    ##Problem 36 — linspace + trig

##Using np.linspace, create 100 points from 0 to 2π. Then compute:

##y1 = sin(t)
##y2 = cos(t)
##y3 = sin(t)² + cos(t)²

##Print the max, min, and mean of y1 using np.max(), np.min(), np.mean(). Then print y3 — what do you notice?

import numpy as np

t = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(t)
y2 = np.cos(t)
y3 = y1**2 + y2**2

print(f"max of y1: {np.max(y1):.4f}")
print(f"min of y1: {np.min(y1):.4f}")
print(f"mean of y1:{np.mean(y1)}")
print("\n[sin(t)]^2 + [cos(t)]^2]:") 
print(f"first 5 value: {y3[:5]}")
print(f"max of y3: {np.max(y3):.8f}")
print(f"min of y3: {np.min(y3):.8f}")
