#Problem 16: Loop over n = 1 to 20. Print only the values of n where n² − n − 1 < 0.
#(This is a simple number filter same idea as filtering speeds, energies, or wavelengths in physics.)

for n in range(1,21):
    if n**2 - n - 1 < 0:
        print(f"n = {n}, n^2 - n - 1 = {n**2 - n - 1}")
