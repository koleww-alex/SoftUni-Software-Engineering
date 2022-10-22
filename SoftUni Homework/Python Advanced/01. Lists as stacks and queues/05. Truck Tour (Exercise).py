from collections import deque

number_of_iterations = int(input())
pumps = deque()

for _ in range(number_of_iterations):
    pump_details = [int(x) for x in input().split()]
    pumps.append(pump_details)

for rotations in range(number_of_iterations):
    tank = 0
    failed = False
    for details in pumps:
        fuel, km = details[0], details[1]
        tank += int(fuel)
        km = int(km)
        if tank >= km:
            tank -= km
        else:
            failed = True
            break
    if failed:
        rotation = pumps.popleft()
        pumps.append(rotation)
    else:
        print(rotations)
        break
