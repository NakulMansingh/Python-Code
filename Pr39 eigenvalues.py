##Problem 39 — eigenvalues

##The inertia tensor of a rigid body is:
    ##I = np.array([
    ##    [3, -1, 0],
    ##    [-1, 3, 0],
    ##    [0,  0, 5]
    ##])

##Find the eigenvalues using np.linalg.eig()
##Print the principal moments of inertia (the eigenvalues)
##Print the principal axes (the eigenvectors)
##Verify: compute I @ v and λ × v for the first eigenpair
    ##and check they're equal (that's the definition of an eigenvector)

import numpy as np

I = np.array([
    [ 3, -1, 0],
    [-1,  3, 0],
    [ 0,  0, 5],
])

vals, vecs = np.linalg.eig(I)

print(f"vals = {vals.round(2)}")
print(f"\nvecs =")
print(vecs.round(3))

print("\nVerification of first eigenpair:")
lam1 = vals[0]
v1 = vecs[:,0] #all rows. 0 column. ==> gives 1st column = 1st eigenvecs
I_v1 = I @ v1
lambda1_v1 = lam1 * v1

print(f"1st eigenvector v1 = {v1.round(4)}")
print(f"I @ v1             = {I_v1.round(4)}")
print(f"lambda_1 * v1      = {lambda1_v1}")
print(f"equal?             = {np.allclose(I_v1, lambda1_v1)}")

