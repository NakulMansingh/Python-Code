#Problem 4 — De Moivre / polar form
#A complex number Z = 3 + 4j.
#Find the modulus r and argument θ (in degrees)
#Verify Euler's formula: reconstruct Z from r and θ using cmath.rect(r, θ_in_radians) and check it matches
#Print both results formatted to 2 decimal places

import math, cmath

z = 3 + 4*1j
r = abs(z)
th = cmath.phase(z)
th_deg = math.degrees(th)
z0 = cmath.rect(r, th)  # it takes r & th to construct z from Eular's formula z = r*e^(j*th). rect = rectangular form

print(f"modulus r = {r:.2f}")
print(f"angle theta = {th_deg:.2f} degrees")
print(f"z(r,th) = {z0:.2f}")
