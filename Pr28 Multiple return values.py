    ##Problem 28 — multiple return values
##Write a function circular_motion(m, r, v) that returns three things:
    ##centripetal acceleration: a = v²/r
    ##centripetal force: F = mv²/r
    ##angular velocity: ω = v/r

##Test with m=2 kg, r=0.5 m, v=3 m/s. Unpack all three return values and print them neatly.

def circular_motion(m,r,v):
    a = v**2 / r
    F = m * v**2 / r
    w = v/r
    return a, F, w
m = 2 ; r = 0.5; v = 3
a, F, w = circular_motion(m,r,v)
print(f"{a, F, w}")
print(f"a = {a} m/s^2 | F = {F} N | w = {w} rad/s")
