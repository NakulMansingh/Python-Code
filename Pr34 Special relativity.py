    ##Problem 34— special relativity

##Write four functions, each building on the previous:
    ##lorentz(v) → γ = 1/√(1 − v²/c²)
    ##rel_momentum(m0, v) → p = γm₀v
    ##rel_energy(m0, v) → E = γm₀c² (total energy)
    ##rel_summary(m0, v) → calls all three, prints γ, p, KE = E − m₀c², and the ratio KE/E

##Then loop over these velocities as fractions of c: 0.1, 0.5, 0.9, 0.99, 0.999
    #and print the full summary for an electron (m₀ = 9.109×10⁻³¹ kg). Watch how KE/E approaches 1 as v → c.

import math

c  = 3e8
m0 = 9.109e-31

def lorentz(v):
    return 1/math.sqrt(1 - (v/c)**2)

def rel_mom(m0,v):
    gamma = lorentz(v)
    return m0 * v * gamma

def rel_En(m0,v):
    gamma = lorentz(v)
    return m0* c**2 *gamma

def rel_summary(m0,v):
    gamma = lorentz(v)
    p = rel_mom(m0,v)
    E = rel_En(m0,v)
    E0 = m0 * c**2
    KE = E - E0
    ratio = KE/E

    print(f"v = {v/c:.3f}c")
    print(f"Lorentz factor         = {gamma:.4f}")
    print(f"Relativistic Momentum  = {p:.4e} kg.m/s")
    print(f"Relativistic Enerrgy   = {E:.4e} J")
    print(f"Kinetic Energy         = {KE:.4e} J")
    print(f"KE/E                   = {ratio:.4f}")
    print("-" * 40)

velocities = [0.1, 0.5, 0.9, 0.99, 0.999]

for beta in velocities:
    rel_summary(m0, beta *c)

#Physics#
    
    #At v = 0.1c, γ ≈ 1 — Newtonian mechanics is perfectly fine.
    #At v = 0.9c, γ = 2.29 — the electron is 2.29× heavier than at rest.
    #At v = 0.999c, γ = 22.37 — the electron would need 22× more force to accelerate than Newton predicts.

    #KE/E → 1 as v → c means almost all the energy is kinetic — the rest energy m₀c² becomes negligible.
    #This is why particle accelerators like the LHC deal in GeV of kinetic energy
        #while the electron rest energy is just 0.511 MeV — the electrons are ultrarelativistic.
