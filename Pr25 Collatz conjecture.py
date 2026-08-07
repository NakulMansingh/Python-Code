#Problem 25 — Collatz conjecture

#Start with any positive integer n. At each step:

    #If n is even → n = n / 2
    #If n is odd → n = 3n + 1

#Keep going until n reaches 1.
    #Print each value and count the steps. Try n = 27.

    #This is a famous unsolved problem in mathematics
        #No one has proven it always reaches 1, but it always has so far.
n = 27
steps = 0

while n != 1:
    if n % 2 == 0: #Checks if n is even or odd. If remainder = 0: It's even.
        n = n//2 #If Even; Replace n to n/2 for the next loop.
    else:
        n = 3 * n + 1
    steps = steps + 1
    print(f"step = {steps:3d}, n = {n}")
    
print(f"\nreached {1} after {steps} steps")
