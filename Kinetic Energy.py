# A proton (mass = 1.6726×10⁻²⁷ kg) moves at 2.5×10⁷ m/s.
#Calculate its kinetic energy in joules, and print it formatted to 3 significant figures in scientific notation.

m = 1.6726e-27 # kg
v = 2.5e7 # m/s
KE = (1/2)*m*v**2
print(f"{KE:.3e}")
