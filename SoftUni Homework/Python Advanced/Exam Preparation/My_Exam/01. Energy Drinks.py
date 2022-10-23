from collections import deque
milligrams_caffeine = deque(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))
max_caffeine = 0

while milligrams_caffeine and energy_drinks:
    caffeine = milligrams_caffeine.pop()
    energy_drink = energy_drinks.popleft()
    result = caffeine * energy_drink

    if result + max_caffeine <= 300:
        max_caffeine += result
    else:
        energy_drinks.append(energy_drink)
        if max_caffeine - 30 < 0:
            max_caffeine = 0
        else:
            max_caffeine -= 30

if energy_drinks:
    print(f'Drinks left: {", ".join(str(x) for x in energy_drinks)}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {max_caffeine} mg caffeine.')
