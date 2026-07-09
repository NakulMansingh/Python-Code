#Problem 12: Given a wavelength lambda in nm,
#print whether it is "visible" (380–700 nm) or "not visible". Test with lam = 500, 100, 800.

#Solution

#Make a list
Lambda = [500, 100, 800]
for L in Lambda:
    if 380 <= L <= 700:
        EM_wv = "Visible"
    else:
        EM_wv = "Not visible"
    print(f"Wavelenght = {L} m, {EM_wv}")
