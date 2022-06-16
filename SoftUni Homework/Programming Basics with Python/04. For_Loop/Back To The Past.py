legacy = float(input())
live_until_year = int(input())
year_cost = 0
current_age = 17
for year in range(1800, live_until_year + 1):
    if year % 2 == 0:
        year_cost += 12000
        current_age += 1
    else:
        current_age += 1
        year_cost += 12000 + (50 * current_age)

if legacy >= year_cost:
    dollars_left = legacy - year_cost
    print(f"Yes! He will live a carefree life and will have {dollars_left:.2f} dollars left.")
else:
    dollars_needed = year_cost - legacy
    print(f"He will need {dollars_needed:.2f} dollars to survive.")
