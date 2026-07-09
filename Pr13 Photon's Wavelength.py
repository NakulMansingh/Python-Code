#Problem 13: Given a photon's wavelength in nm, classify it:

#< 10 → X-ray
#10–400 → ultraviolet
#400–700 → visible
#700–1000 → infrared
#1000 → microwave

#Test with lam = 5, 250, 550, 850, 5000.

#Solution

Wavelenghts = [5, 250, 550, 850, 5000]
for Wv in Wavelenghts:
    if Wv < 10:
        tag = "X-rays"
    elif 10 <= Wv < 400:
        tag = "UV"
    elif 400 <= Wv < 700:
        tag = "Visible"
    elif 700 <= Wv < 1000:
        tag = "IF"
    else:
        tag = "Microwave"
    print(f"Wavelenght = {Wv} nm, range = {tag}")
