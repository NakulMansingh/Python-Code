#Problem 2 — if/elif/else: gravitational zones
#Given a distance r from Earth's centre (in km), classify the region and print the approximate gravitational acceleration:
#Region, r (km), g (m/s²)
#Inner core, r < 1220, 4.4
#Outer core, r < 3480, g = 9.0
#Mantle, r < 6371, g = 9.8
#Low orbit, r < 8000, g = 7.3
#Deep space, r ≥ 8000, g ~ 0
#Test with r = 500, 2000, 5000, 7000, 50000.

#Solution
# Make a list
Radius = [500, 2000, 5000, 7000, 50000]

for r in Radius:
    if r < 1221:
        region = "Inner core"
        g = 4.4
    elif r < 3481:
        region = "Outer core"
        g = 9.0
    elif r < 6372:
        region = "Mantle"
        g = 9.8
    elif r < 8001:
        region = "Low orbit"
        g = 7.3
    else:
        region = "Deep space"
        g = 0.0
    print(f"r = {r:6d} km, {region:<12} g = {g} m/s^2")

#{r:6d} — the 6 means "pad to 6 characters wide".
#This right-aligns all the numbers so the output forms a neat column. Without it, the spacing would be ragged.
    
#{region:<12} — the < means left-align, padded to 12 characters wide.
#So "inner core", "mantle", "deep space" all take the same horizontal space, keeping the g = column lined up neatly.

#Together these are called field width specifiers — very handy whenever you're printing a table of results.
#The pattern is {value:[<>]width[.precision][type]}.
