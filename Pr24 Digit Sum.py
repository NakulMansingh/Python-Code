#Problem 2 — digit sum

#Take any number, say 9875. Repeatedly add its digits until you get a single digit number. Print each step.

    #9875 → 9+8+7+5 = 29
    #29   → 2+9 = 11
    #11   → 1+1 = 2
    #Single digit reached: 2

#Hint: str(n) converts a number to string. int(d) converts a character back to integer.
#You can loop over digits of a string with for d in str(n).

n = 9875
while n >= 10:
    total = 0
    for d in str(n):
        digit = int(d)
        total = total + digit
    print(f"{n}: total = {total}")
    n = total
print(f"single digit reached: {n}")
    
