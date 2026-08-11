    ##Problem 31 — Schwarzschild radius

##Write two functions:
    ##schwarzschild_radius(M) → r = 2GM/c² (G=6.674×10⁻¹¹, c=3×10⁸)
    ##is_black_hole(M, R) → returns True if the object's radius R is smaller than its Schwarzschild radius, False otherwise

##Then loop over these objects and print whether each is a black hole:

    ## objects = [
    ##    ("Sun",         1.989e30, 6.963e8),
    ##    ("Earth",       5.972e24, 6.371e6),
    ##    ("Neutron star",2.0e30,   1.0e4  ),
    ##    ("Stellar BH",  2.0e31,   1.0e3  ),
    ## ]

def schwarzschild_radius(M):
    c = 3e8
    G = 6.674e-11
    return 2*G*M/c**2

def black_hole(M,R):
    rs = schwarzschild_radius(M)
    return R < rs

objects = [
    ("Sun",         1.989e30, 6.963e8),
    ("Earth",       5.972e24, 6.371e6),
    ("Neutron star",2.0e30,   1.0e4  ),
    ("Stellar BH",  2.0e31,   1.0e3  ),
]

for o, M, R in objects:
    rs = schwarzschild_radius(M)
    BH = black_hole(M,R)
    tag = "Black Hole" if BH else "Not a Black Hole"
    print(f"{o:<15} rs = {rs:.2e} m   -->   {tag}")
    
    
    
