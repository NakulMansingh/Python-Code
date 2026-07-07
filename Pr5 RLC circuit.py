#Problem 5 — RLC circuit
#In a series RLC circuit, total impedance is Z = R + j(ωL − 1/ωC).
#Given: R = 50 Ω, L = 0.1 H, C = 1×10⁻⁵ F, ω = 1000 rad/s
#Compute Z
#Find the resonant frequency ω₀ = 1/√(LC) using math.sqrt()
#Print magnitude and phase of Z, and the resonant frequency, all formatted neatly

import math, cmath

R = 50      #ohms
L = 0.1     #Henrys
C = 1e-5    #Farads
w = 1000    #rad/s

z = R + (w*L - 1/(w*C))*1j
w0_sq = 1/(L*C)
w0 = math.sqrt(w0_sq)
z_mag = abs(z)
ph = math.degrees(cmath.phase(z))

print(f"z = {z}")
print(f"|z| = {z_mag:.2f} ohms")
print(f"phase = {ph:.2f} degrees")
print(f"resonant frequency w0 = {w0:.2f} rad/s")
