#In an AC circuit, the impedance of a resistor and inductor in series is Z = R + jωL. Given R = 100 Ω, L = 0.05 H, ω = 2000 rad/s:
#1. Compute Z as a Python complex number
#2. Print the magnitude |Z| formatted to 2 decimal places
#3. Print the phase angle in degrees, formatted to 2 decimal places

import math, cmath
R = 100     #ohms
L = 0.05    #Henry
w = 2000    #rad/s

z = R + L*w*1j   # I could've written z = complex(R, L*w)
mag = abs(z)
ph = math.degrees(cmath.phase(z))   # tan(ang) = L*w/R
#cmath.phase calculates the phase in radians and math.degrees changes that in degrees.

print(f"z = {z}")
print(f"magnitude = {mag:.2f} ohms")
print(f"phase = {ph} degrees")
