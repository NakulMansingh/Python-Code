    ##Problem 3 — rocket equation

##Write three functions:
    ##delta_v(ve, m0, mf) → Δv = ve × ln(m0/mf) (Tsiolkovsky rocket equation)
    ##fuel_required(ve, m0, dv) → mf = m0 × e^(−dv/ve), fuel = m0 − mf
    ##rocket_summary(name, ve, m0, mf) → calls both, prints Δv and fuel fraction

##Test with:

    ##rockets = [
    ##    ("Saturn V",     2580, 2.97e6, 1.3e5),
    ##    ("Falcon 9",     3050, 5.49e5, 1.0e4),
    ##    ("Ion thruster", 30000, 1000,   900 ),
    ##]
import math

def delta_v(ve, m0, mf):
    return ve* math.log(m0/mf)

def fuel_required(ve, m0, dv):
    mf   = m0* math.exp(-dv/ve)
    fuel = m0 - mf
    return fuel

def roc_summary(rocket, ve, m0, mf):
    dv         = delta_v(ve, m0, mf)
    fuel       = fuel_required(ve, m0, dv)
    fuel_frac  = fuel/m0 *100
    
    print(f"rocket:         {rocket}")
    print(f"dv:             {dv/1000:.2f} km/s")
    print(f"fuel fraction:  {fuel_frac:.1f}%")
    print("-" * 40)

rockets = [
    ("Saturn V", 2580, 2.97e6, 1.3e5),
    ("Falcon 9", 3050, 5.49e5, 1.0e4),
    ("Ion Thruster", 30000, 1000, 900),
]

for rocket, ve, m0, mf in rockets:
    roc_summary(rocket, ve, m0, mf)

##The physics tells a striking story:
    
##1
    #The Saturn V burns 95.6% of its mass as fuel — only 4.4% reaches orbit.
    #The Falcon 9 is even more extreme at 98.2%. This is why rocket engineering is so brutally hard.
    #You're mostly launching fuel to burn more fuel.

##2
    #The ion thruster burns only 10% of its mass — incredibly efficient.
    #But its Δv of 3.16 km/s seems low.
    #The trick is ion thrusters run continuously for months or years in space, accumulating enormous Δv over time.
    #They just can't lift off from Earth.

#This is the tyranny of the rocket equation — Tsiolkovsky derived it in 1903, and nothing has changed the fundamental physics since.
