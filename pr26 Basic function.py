    #Problem 26 — basic function

#Write a function wave_speed(f, lam) that takes frequency f (Hz) and wavelength lam (m) and returns wave speed v = fλ.

#Test it with:
    #f=440 Hz, λ=0.773 m (A note in air)
    #f=2.4e9 Hz, λ=0.125 m (microwave)

def wv_speed(f,l):
    return f*l
print(f"v_air = {wv_speed(440,0.773)} m/s")
print(f"v_microwave = {wv_speed(2.4e9,0.125):.2e} m/s")
