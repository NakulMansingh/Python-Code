#Problem 14: Given a star's surface temperature T (in Kelvin), print its spectral class:

#T > 30000 → class O
#T > 10000 → class B
#T > 7500 → class A
#T > 6000 → class F
#T > 5200 → class G (our Sun)
#T > 3700 → class K
#else → class M

#Test with T = 40000, 15000, 9000, 7000, 5800, 4500, 3000.

Temperature = [40000, 15000, 9000, 7000, 5800, 4500, 3000]
for T in Temperature:
    if T > 30000:
        spectral = "class O"
    elif T > 10000:
        spectral = "class B"
    elif T > 7500:
        spectral = "class A"
    elif T > 6000:
        spectral = "class F"
    elif T > 5200:
        spectral = "class G (The Sun)"
    elif T > 3700:
        spectral = "class K"
    else:
        spectral = "class M"
        
    print(f" Temperature = {T:5d} Kelvin, spectral {spectral}")
