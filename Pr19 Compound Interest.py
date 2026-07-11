#Problem 19 — compound interest
#You deposit ₹10,000 in a bank at 8% interest per year. Write a while loop that keeps adding interest each year until the amount doubles.
#Print the amount at the end of each year, and how many years it took.

m = 10000
initial = 10000
years = 0
while m < initial * 2:
    m += m * 0.08
    years += 1
    print(f"year = {years}, $ = {m:.2f}")
print(f"doubled in {years} years")
