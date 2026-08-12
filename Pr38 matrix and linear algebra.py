    ##Problem 4 — matrix and linear algebra

##A system of 3 equations (Kirchhoff's voltage law in a circuit):

    ##2I₁ +  I₂        = 5
    ## I₁ + 3I₂ +  I₃  = 10
    ##        I₂ + 2I₃  = 4

##Write this as Ax = b and solve using np.linalg.solve().
##Print each current I₁, I₂, I₃.

import numpy as np

A = np.array([
    [2,1,0],
    [1,3,1],
    [0,1,2]
])

b = np.array([5, 10, 4])

I = np.linalg.solve(A,b)
print(f"[I1, I2, I3] = {I}")
