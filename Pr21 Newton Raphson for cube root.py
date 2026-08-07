#Problem 21 — Newton-Raphson for cube root


#Adapt the Newton-Raphson method to find the cube root of 50. The update rule for solving x³ = 50 is:
    #x_new = x − (x³ − 50) / (3x²)

#Start with x = 5.0, tolerance = 1e-8. Print x at each step and the number of iterations.

x = 5.0 #Initial guess. We pick 5 because 5³ = 125, which is reasonably close to 50.
tolerance = 1e-8
iteration = 0

while abs(x**3 - 50) > tolerance:
#x**3 - 50 is the error — how far x³ is from 50. When this drops below 1e-8, we're close enough.
#abs() keeps it positive.
    x_new = x - (x**3 - 50)/(3*x**2) #x_new = x - f(x)/f'(x) Newton-Raphson
    x = x_new
    iteration = iteration + 1
    print(f"iterations = {iteration}: x = {x:.6f}: error = {abs(x**3 - 50):.4e}")
print(f"cube root of 50 is {x:.5f}")
print(f"converged in {iteration} iterations")
