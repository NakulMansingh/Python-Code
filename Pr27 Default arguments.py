    #Problem 2 — default arguments

#Write a function pendulum_period(L, g=9.81) that returns T = 2π√(L/g).

#Test it with:
    #L=1.0 m on Earth (g=9.81)
    #L=1.0 m on Moon (g=1.62)
    #L=1.0 m on Mars (g=3.72)

#Print all three periods formatted to 3 decimal places.

def pendulum_period(L, g=9.81):
    import math
    return 2 * math.pi * math.sqrt(L/g)
print(f"period (Earth) = {pendulum_period(1):.3f}")
print(f"period (Moon) = {pendulum_period(1,1.62):.3f}")
print(f"period (Mars) = {pendulum_period(1,3.72):.3f}")
