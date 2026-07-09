#Problem 11: Given a temperature T in Kelvin,
#print "above absolute zero" if T > 0, and "absolute zero or below" if T ≤ 0. Test with T = 300, 0, -5.

#Solution

#Make a list
T = [300, 0, -5]

for t in T:
    if t > 0:
        temp = "above absolute zero"
    else:
        temp = "absolute zero or below"
    print(f"Temperature = {t}, {temp}")
    
