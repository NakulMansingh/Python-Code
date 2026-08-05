#Problem 6 — Damped oscillator
#The complex frequency of a damped harmonic oscillator is: ω_complex = −jγ/2 ± √(ω₀² − γ²/4)
#where ω₀ = 10 rad/s (natural frequency) and γ = 3 rad/s (damping coefficient).
#Compute both roots (+ and − cases) as complex numbers — use cmath.sqrt() since the expression under the root could go negative
#Print the real part (oscillation frequency) and imaginary part (decay rate) of each root
#Check: is this oscillator underdamped (γ < 2ω₀), critically damped (γ = 2ω₀), or overdamped (γ > 2ω₀)?

import math, cmath

w0 = 10 #rad/s
y = 3 #rad/s

im_part = -y*1j/2
re_part = cmath.sqrt(w0**2 - (y**2)/4)

p_root = im_part + re_part
n_root = im_part - re_part

if y < 2*w0 :
    regime = "underdamped oscillator"
elif y == 2*w0 :
    regime = "critically damped oscillator"
else:
    regime = "overdamped oscillator"

print(f"positive root = {p_root:.2f}, negative root = {n_root:.2f}")
print(f"oscillation frequency = {re_part.real:.2f}, decay rate = {im_part.imag:.2f}")
print(f"regime = {regime} because y = {y}, 2w0 = {2*w0}")
