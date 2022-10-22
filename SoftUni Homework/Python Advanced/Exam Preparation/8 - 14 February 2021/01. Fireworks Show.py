from collections import deque

fireworks = deque(map(int, input().split(', ')))
explosives = deque(map(int, input().split(', ')))

types_of_fireworks = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0,
}
show_time = False
while fireworks and explosives:
    firework = fireworks[0]
    explosive = explosives[-1]

    if firework <= 0:
        fireworks.popleft()
        continue
    elif explosive <= 0:
        explosives.pop()
        continue

    total = firework + explosive

    if total % 3 == 0 and total % 5 != 0:
        types_of_fireworks['Palm Fireworks'] += 1
        fireworks.popleft(), explosives.pop()

    elif total % 5 == 0 and total % 3 != 0:
        types_of_fireworks['Willow Fireworks'] += 1
        fireworks.popleft(), explosives.pop()

    elif total % 3 == 0 and total % 5 == 0:
        types_of_fireworks['Crossette Fireworks'] += 1
        fireworks.popleft(), explosives.pop()

    else:
        fireworks[0] -= 1
        fireworks.append(fireworks.popleft())

    show = [x for x in types_of_fireworks.values() if x >= 3]
    if len(show) == 3:
        print('Congrats! You made the perfect firework show!')
        show_time = True
        break

if not show_time:
    print("Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f'Firework Effects left: {", ".join(str(x) for x in fireworks)}')

if explosives:
    print(f'Explosive Power left: {", ".join(str(x) for x in explosives)}')

for key, val in types_of_fireworks.items():
    print(f'{key}: {val}')
