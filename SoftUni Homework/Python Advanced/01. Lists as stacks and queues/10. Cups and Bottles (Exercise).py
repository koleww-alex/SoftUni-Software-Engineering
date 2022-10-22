from collections import deque
cups_of_water = deque(list(map(int, input().split())))
bottles_of_water = list(map(int, input().split()))
wasted_liters_of_water = 0

for _ in range(len(cups_of_water)):

    for _ in range(len(bottles_of_water)):

        if bottles_of_water[-1] > cups_of_water[0]:
            wasted_liters_of_water += bottles_of_water[-1] - cups_of_water[0]
            cups_of_water.popleft()
            bottles_of_water.pop()
            break

        elif bottles_of_water[-1] == cups_of_water[0]:
            cups_of_water.popleft()
            bottles_of_water.pop()
            break

        else:
            cups_of_water[0] -= bottles_of_water[-1]
            bottles_of_water.pop()
            if cups_of_water[0] <= 0:
                cups_of_water.popleft()


if bottles_of_water:
    print(f'Bottles: {" ".join(str(x) for x in bottles_of_water)}')
    print(f'Wasted litters of water: {wasted_liters_of_water}')
else:
    print(f'Cups: {" ".join(str(x) for x in cups_of_water)}')
    print(f'Wasted litters of water: {wasted_liters_of_water}')
