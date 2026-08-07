#Problem 20 — Skydiver falls with air drag

#A skydiver falls. Each second, gravity adds 9.81 m/s to their velocity,
#but air resistance removes 10% of their current velocity. Starting from v = 0:

#Loop until velocity stops changing by more than 0.01 m/s per second (that's terminal velocity)
#Print velocity each second
#Print how many seconds it took to reach terminal velocity

#Terminal velocity should come out near 98.1 m/s.

v = 0
t = 0
change = 9.81 #Tolerance

while change > 0.01: #This is the condition for the loop to go on.
    v_new = v + 9.81 - 0.1 * v
    change = abs(v_new - v)
    v = v_new
    t = t + 1
    print(f"v = {v_new:.2f} m/s at t = {t:.0f} sec, dv by = {change:.2f} m/s")
    
print(f"Terminal velocity {v:.2f} achieved in {t:.0f} sec")
    
