#Problem 10 — for loop + if: Bohr energy levels
#The energy of the nth Bohr orbit is Eₙ = −13.6/n² eV. Loop over n = 1 to 10 and:
#Print Eₙ for each level formatted to 4 decimal places
#If the transition from n → n−1 releases a photon, print the photon energy ΔE = Eₙ₋₁ − Eₙ as well (skip n=1 since there's no n=0)
#Mark with *** visible light *** if 1.8 eV ≤ ΔE ≤ 3.1 eV

for n in range(1, 11):
    E_n = -13.6 / n**2

    if n > 1:
        E_prev = -13.6 / (n-1)**2
        dE = E_n - E_prev

        if 1.8 <= dE <= 3.1:
            tag = "visible light is released"
        else:
            tag = ""
            
        print(f"n = {n:2d}, En = {E_n:4f} eV, dE = {dE:.3f} eV, {tag}")
    else:
        print(f"n = {n}, En = {E_n:4f} eV")
        
