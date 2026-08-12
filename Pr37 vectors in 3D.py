    ##Problem 27 — vectors in 3D

##Two forces act on a particle:
    ##F1 = [3, -2, 5] N
    ##F2 = [-1, 4, 2] N

##Using NumPy:
    ##Find the resultant force F = F1 + F2
    ##Find the magnitude |F|
    ##Find the unit vector F̂
    ##Find the angle between F1 and F2 using: cos θ = F1·F2 / (|F1||F2|)

##Print the angle in degrees. You'll need np.arccos() and np.degrees().

import numpy as np

F1 = np.array([3, -2, 5])
F2 = np.array([-1, 4, 2])

F = F1 + F2
magF = np.linalg.norm(F)
F_hat = F/magF
F1F2 = np.dot(F1,F2)

magF1 = np.linalg.norm(F1)
magF2 = np.linalg.norm(F2)

cos_theta = F1F2 / (magF1 * magF2)

ang = np.arccos(cos_theta)
theta = np.degrees(ang) #Alternate #theta = np.degrees(np.arccoss(cos_theta))
    
print(f"F = F1 + F2: {F}")
print(f"magnitude |F| = {magF:.2f}")
print(f"Unit Vector F = {F_hat.round(4)}")
print(f"\nF1.F2 = {F1F2}")
print(f"|F1| = {magF1:.4f}")
print(f"|F2| = {magF2:.4f}")
print(f"Angle between F1 & F2: {theta:.2f} deg")



