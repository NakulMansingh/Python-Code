#Problem 3 — free fall with air resistance
#A skydiver falls. Each second, gravity adds 9.81 m/s to their velocity, but air resistance removes 10% of their current velocity. Starting from v = 0:

#Loop until velocity stops changing by more than 0.01 m/s per second (that's terminal velocity)
#Print velocity each second
#Print how many seconds it took to reach terminal velocity

#Terminal velocity should come out near 98.1 m/s.


#Give the starter for the loop

v = 0.0         #The skydiver starts from rest. Velocity is 0 at t=0.
t = 0           #Timer starts at 0. This counts how many seconds have passed.
dv = 9.81       # change #The while loop checks change > 0.01 before running even once.
                #But change doesn't exist yet — so we set it to a large number (9.81) just to enter the loop.

#these values will go into the loop in begining
#Loop will modify them after each iteration

while dv > 0.01:
    v_new = v + 9.81 - 0.1 * v  #Result stored in v_new, not v yet — because we need the old v on the next line to measure the change.
    dv = abs(v_new - v)         #abs() makes it positive. This is what the while condition checks next time around.
    v = v_new                   #Now overwrite v with the new value. We waited until after measuring change to do this.
    t += 1
    print(f"at t = {t}sec, v = {v} m/s, dv = {dv} m/s")
print(f"terminal velocity = {v} sec after {t} sec")
