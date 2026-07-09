#Problem 17: The escape velocity from a planet is v = √(2GM/R)
#Loop over this list of planets and print only those a 10 km/s rocket canescape from:

import math

Planets = [
    ("Mercuray", 3.285e23, 2.439e6),
    ("Venus",    4.867e24, 6.051e6),
    ("Earth",    5.972e24, 6.371e6),
    ("Mars",     6.390e23, 3.389e6),
    ("Jupiter",  1.898e27, 6.991e7)
]
#Rocket escape velocity is 10 km/s.
G = 6.674e-11

for p, M, R in Planets:
    v_esc = math.sqrt(2*G*M/R) /1000 #escape velocity in km/s
    if v_esc < 10:
        print(f"rocket can escape   {p:<8} because v_escape = {v_esc:.2f} km/s")
    else:
        print(f"rocket can't escape {p:<8} because v_escape = {v_esc:.2f} km/s")
