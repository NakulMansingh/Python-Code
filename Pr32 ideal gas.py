    ##Problem 32 — ideal gas

##Write three functions:
    ##pressure(n, T, V) → P = nRT/V (R = 8.314 J/mol·K)
    ##rms_speed(M, T) → v = √(3RT/M) (M = molar mass in kg/mol)
    ##gas_summary(n, T, V, M, name) → calls both and prints neatly

##Test with 1 mol of:
    ##Hydrogen (M = 0.002 kg/mol) at 300 K in 0.025 m³
    ##Oxygen (M = 0.032 kg/mol) at 300 K in 0.025 m³
    ##Helium (M = 0.004 kg/mol) at 500 K in 0.010 m³
import math

def pressure(n,T,V):
    R = 8.314 #J/mol.K
    return n*R*T/V

def rms_speed(M,T):
    R = 8.314 #J/mol.K
    return math.sqrt(3*R*T/M)

def gas_summary(n,T,V,M,gas):
    P = pressure(n,T,V)
    v = rms_speed(M,T)
    return P, v

gases = [
    (1, "Hydrogen", 0.002, 300, 0.025),
    (1, "Oxygen",   0.032, 300, 0.025),
    (1, "Helium",   0.004, 500, 0.010),
]

for n, gas, M, T, V in gases:
    P, v = gas_summary(n,T,V,M,gas) 
    print(f"{gas:<8}, Pressure = {P:.2f} Pa, rms_speed = {v:.2f} m/s")
