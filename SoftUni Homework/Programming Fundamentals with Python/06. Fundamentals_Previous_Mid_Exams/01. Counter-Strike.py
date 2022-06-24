total_energy = int(input())
command = input()
won_battles = 0
energy_left = True
while command != "End of battle":
    distance = int(command)
    if total_energy >= distance:
        total_energy -= distance
        won_battles += 1
        if won_battles % 3 == 0:
            total_energy += won_battles
    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {total_energy} energy")
        energy_left = False
        break

    command = input()

if energy_left:
    print(f"Won battles: {won_battles}. Energy left: {total_energy}")
