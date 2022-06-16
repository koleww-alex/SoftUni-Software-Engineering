x = int(input())
y = float(input())
z = int(input())
number_workers = int(input())
from math import floor, ceil

grapes_meter = x * y
liters_wine = grapes_meter / 2.5 * 0.4

if liters_wine >= z:

    print(f"Good harvest this year! Total wine: {floor(liters_wine)} liters.")
    print(f"{liters_wine - z:.0f} liters left -> {ceil((liters_wine - z) / number_workers)} liters per person.")

else:
    print(f"It will be a tough winter! More {floor(z - liters_wine)} liters wine needed.")
