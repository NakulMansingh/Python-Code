    ##Problem 36 — your first array

##Create a NumPy array of velocities: [0, 5, 10, 15, 20, 25, 30] m/s.
##Then compute and print:
    ##KE for each velocity (m = 2 kg)
    ##Momentum for each velocity (m = 2 kg)
    ##Only the velocities where KE > 200 J (boolean masking)

import numpy as np

m = 2
v = np.array([0, 5, 10, 15, 20, 25, 30])
KE = 0.5 * m * v**2
p = m * v

print("velocity (m/s):", v)
print("KE (J)        :", KE)
print("Momentum      :", p)
print("\nVelocities where KE > 200 J")
print(v[KE > 200])

