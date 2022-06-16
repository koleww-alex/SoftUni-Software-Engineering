x = int(input())
y = float(input())
z = int(input())
number_workers = int(input())
from math import floor, ceil

grapes_meter = x * y
liters_wine = grapes_meter / 2.5 * 0.4

if liters_wine >= z:
    floor(liters_wine)
    ceil(liters_wine - z)
    ceil((liters_wine - z) / number_workers)
    print(f"Good harvest this year! Total wine: {liters_wine:.0f} liters.")
    print(f"{liters_wine - z:.0f} liters left -> {(liters_wine - z) / number_workers:.0f} liters per person.")

else:
    liters_needed = floor(z - liters_wine)
    print(f"It will be a tough winter! More {liters_needed:.0f} liters wine needed.")