#Problem 6 — Damped oscillator
#The complex frequency of a damped harmonic oscillator is: ω_complex = −jγ/2 ± √(ω₀² − γ²/4)
#where ω₀ = 10 rad/s (natural frequency) and γ = 3 rad/s (damping coefficient).
#Compute both roots (+ and − cases) as complex numbers — use cmath.sqrt() since the expression under the root could go negative
#Print the real part (oscillation frequency) and imaginary part (decay rate) of each root
#Check: is this oscillator underdamped (γ < 2ω₀), critically damped (γ = 2ω₀), or overdamped (γ > 2ω₀)?

import math, cmath

w0 = 10     # natural frequency rad/s
y = 3       # damping rate rad/s

im_part = -y*1j/2
re_part = cmath.sqrt(w0**2 - (y**2)/4)

pos_root = re_part + im_part
neg_root = - re_part + im_part

print(f"positive root = {pos_root:.2f}")
print(f"negative root = {neg_root:.2f}")
print(f"oscillation frequency = {re_part:.2f}")
print(f"decay rate = {im_part:.2f}")

if y < 2*w0:
    regime = "oscillator underdamped"
elif y == 2*w0:
    regime = "oscillator critially damped"
else:
    regime = "oscillator overdamped"
print(f"regime ={regime} because y = {y}, 2w0= {2*w0}")
