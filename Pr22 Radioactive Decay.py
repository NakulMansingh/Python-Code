#Problem 22 — radioactive decay

#A radioactive sample starts with N₀ = 1000 atoms. Each second, 5% of the remaining atoms decay.
#Write a while loop that runs until fewer than 10 atoms remain.
#Print the number of atoms and time at each step, and the total time taken.

#The half-life formula says t½ = ln(2)/0.05 ≈ 13.86 s — check if your loop agrees.

import math
N = 1000
tolerance = 10
t = 0

while N > 10:
    N_new = N  - N * 0.05
    N = N_new
    t = t +1
    print(f"Atoms left = {N_new:.2f}: at t = {t:.2f} s")
print(f"\nFewer than 10 atoms reached at t={t}s") # \n : give a space b/w lines in the results
print(f"\nVerification:")
print(f"Half-life formula:  t½ = {math.log(2)/0.05:.2f}s")
print(f"100 atoms at t =    {math.log(1000/100)/0.05:.2f}s  (from formula)")
print(f"10 atoms at t  =    {math.log(1000/10)/0.05:.2f}s  (from formula)")
