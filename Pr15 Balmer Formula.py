#Problem 5: Loop over n = 1 to 8 and print the wavelength of each hydrogen spectral line using the Balmer formula:
#1/λ = R × (1/4 − 1/n²), where R = 1.097×10⁷ m⁻¹, and n starts from 3.
#So loop n = 3, 4, 5 ... 8 and print λ in nm.

R = 1.097e7 #Rydberg's constant 1/m

for n in range(3, 9):
    L = 1/(R*(1/4 - 1/n**2))
    L_nm = L * 1e9
    print(f"n = {n}, Wavelenght = {L_nm:.0f} nm")
