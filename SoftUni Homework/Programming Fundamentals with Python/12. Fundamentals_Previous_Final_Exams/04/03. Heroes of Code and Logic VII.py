number_of_iterations = int(input())
heroes = {}
for _ in range(number_of_iterations):
    info = input().split()
    hero, hp, mp = info[0], info[1], info[2]
    if hero not in heroes:
        heroes[hero] = [int(hp), int(mp)]

command = input()
while command != 'End':
    current_command = command.split(' - ')
    operation = current_command[0]
    if operation == 'CastSpell':
        hero, mp_needed, spell = current_command[1], int(current_command[2]), current_command[3]
        if heroes[hero][1] >= mp_needed:
            heroes[hero][1] -= mp_needed
            print(f'{hero} has successfully cast {spell} and now has {heroes[hero][1]} MP!')
        else:
            print(f'{hero} does not have enough MP to cast {spell}!')
    elif operation == 'TakeDamage':
        hero, damage, attacker = current_command[1], int(current_command[2]), current_command[3]
        if heroes[hero][0] > damage:
            heroes[hero][0] -= damage
            print(f'{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0]} HP left!')
        else:
            del heroes[hero]
            print(f'{hero} has been killed by {attacker}!')
    elif operation == 'Recharge':
        hero, amount = current_command[1], int(current_command[2])
        if heroes[hero][1] + amount > 200:
            amount = 200 - heroes[hero][1]
            heroes[hero][1] = 200
        else:
            heroes[hero][1] += amount
        print(f'{hero} recharged for {amount} MP!')
    elif operation == 'Heal':
        hero, amount = current_command[1], int(current_command[2])
        if heroes[hero][0] + amount > 100:
            amount = 100 - heroes[hero][0]
            heroes[hero][0] = 100
        else:
            heroes[hero][0] += amount
        print(f'{hero} healed for {amount} HP!')

    command = input()

for hero in heroes:
    print(hero)
    print(f'HP: {heroes[hero][0]}')
    print(f'MP: {heroes[hero][1]}')
