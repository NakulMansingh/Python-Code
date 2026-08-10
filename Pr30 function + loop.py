    ##Problem 30 — function + loop

##Write a function bohr_energy(n) that returns Eₙ = −13.6/n² eV.
    ##Then write a second function emission_wavelength(n1, n2) that:

    ## 1. Calls bohr_energy() for both levels
    ## 2. Computes ΔE = E(n2) − E(n1) in eV
    ## 3. Converts to wavelength: λ = hc/ΔE (use h=4.136×10⁻¹⁵ eV·s, c=3×10⁸ m/s)
    ## 4. Returns λ in nm

##Finally, loop over all transitions from n=3,4,5,6 down to n=2 (Balmer series) and print the wavelength of each.
##You solved this before with a formula — now do it properly with functions.

def bohr_energy(n):
    return -13.6/n**2

def emission_wavelength(n1,n2):
    E1 = bohr_energy(n1)
    E2 = bohr_energy(n2)
    dE = E2 - E1
    h = 4.136e-15 #eV.s
    c = 3e8 #m/s
    lam = h*c/abs(dE)
    lam_nm = lam * 1e9 #nm
    return lam_nm

for n in range(3,7):
    lam = emission_wavelength(n,2)
    print(f"n = {n} -> 2, lambda = {lam:.1f} nm")
