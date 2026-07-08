#Problem 9 — for loop: Coulomb's law table
#Two charges q₁ = 1.6×10⁻¹⁹ C and q₂ = 1.6×10⁻¹⁹ C (two protons).
#Using Coulomb's law F = kq₁q₂/r²,
#print a table of force vs distance for r = 1×10⁻¹⁵ m to 5×10⁻¹⁵ m in steps of 1×10⁻¹⁵ (k = 8.99×10⁹).

q1 = 1.6e-15
q2 = 1.6e-19
k = 8.99e9

#for Loop
for i in range(1,6):
    r = i * 1e-15
    F = k*q1*q2/r**2
    print(f"r = {r:.1e} m, F = {F:.3e} N")
