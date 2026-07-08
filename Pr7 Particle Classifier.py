#Problem 1 — if/elif/else: particle classifier
#Given a particle's charge q (in units of elementary charge) and mass m (in MeV/c²), classify it:
#q = +1, m = 938.3 → proton
#q = -1, m = 0.511 → electron
#q = 0, m = 939.6 → neutron
#q = 0, m = 0 → photon
#Write if/elif/else logic that prints the particle name. Test all 4 cases.

#Solution
# Make a list
particles = [
    (+1, 938.3),
    (-1, 0.511),
    ( 0, 939.6),
    ( 0, 0.0  )
]
#if and else statement now

for q, m in particles:
    if q == +1 and m > 900:
        name = "proton"
    elif q == -1 and m < 1:
        name = "electron"
    elif q == 0 and m > 900:
        name = "neutron"
    elif q == 0 and m == 0:
        name = "photon"
    else:
        name = "unknown particle"
    print(f"q = {q:+d}, m = {m:.3f}, particle = {name}")
