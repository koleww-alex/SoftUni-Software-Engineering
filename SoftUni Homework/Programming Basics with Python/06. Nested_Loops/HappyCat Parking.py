number_days = int(input())
number_hours = int(input())
total_tax = 0

for day in range(1, number_days + 1):
    tax_per_hour = 0
    for hours in range(1, number_hours + 1):

        if day % 2 == 0 and hours % 2 != 0:
            tax_per_hour += 2.50

        elif day % 2 != 0 and hours % 2 == 0:
            tax_per_hour += 1.25

        else:
            tax_per_hour += 1.00
    print(f"Day: {day} – {tax_per_hour:.2f} leva")
    total_tax += tax_per_hour

print(f"Total: {total_tax:.2f} leva")
