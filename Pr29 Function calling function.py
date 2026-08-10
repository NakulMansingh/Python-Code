    ##Problem 29 — function calling function

##Write two functions:
    ##coulomb_force(q1, q2, r) → F = kq₁q₂/r² (k = 8.99×10⁹)
    ##coulomb_pe(q1, q2, r) → U = kq₁q₂/r

##Then write a third function coulomb_summary(q1, q2, r) that calls both and prints:
    ##r = 1.00e-10 m
    ##F = 2.307e-08 N
    ##U = -2.307e-18 J

##Test with two protons (q = 1.6×10⁻¹⁹ C) at r = 1×10⁻¹⁰ m, and one proton + one electron at the same distance.

def coulomb_force(q1,q2,r):
    k = 9e9
    return k*q1*q2/r**2

def coulomb_pot(q1,q2,r):
    k = 9e9
    return k*q1*q2/r

def coulomb_summary(q1,q2,r):
    F = coulomb_force(q1,q2,r)
    U = coulomb_pot(q1,q2,r)
    print(f"r = {r:.2e} m")
    print(f"F = {F:.2e} N")
    print(f"U = {U:.2e} J")

r = 1e-10
q_proton = 1.6e-19
q_electron = - 1.6e-19

print("two protons")
coulomb_summary(q_proton, q_proton, r)

print("\nproton + electron")
coulomb_summary(q_proton, q_electron, r)
