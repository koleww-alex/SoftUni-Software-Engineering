water_capacity = 255
n = int(input())

filling_the_tank = 0

for _ in range(1, n + 1):
    liters_of_water = int(input())

    if filling_the_tank + liters_of_water > water_capacity:
        print("Insufficient capacity!")
        continue

    filling_the_tank += liters_of_water

print(filling_the_tank)
