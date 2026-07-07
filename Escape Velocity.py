#Problem 2 — Escape velocity
#Escape velocity is given by v = √(2GM/R).
#Write the variables for Earth (M = 5.972×10²⁴ kg, R = 6.371×10⁶ m, G = 6.674×10⁻¹¹).
#ompute escape velocity, and print it as: Escape velocity = 11184.9 m/s.

M = 5.972e24    #kg
G = 6.674e-11   #Gravitation const
R = 6.371e6     #m
v_sq = 2*G*M/R
import math
v = math.sqrt(v_sq)  #m/s
print(f"{v:.1f} m/s")
