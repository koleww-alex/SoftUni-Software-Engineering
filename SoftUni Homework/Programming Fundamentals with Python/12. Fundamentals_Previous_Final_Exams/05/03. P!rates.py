cities_info = {}
command = input()
while command != 'Sail':
    current_command = command.split('||')
    city, population, gold = current_command[0], int(current_command[1]), int(current_command[2])
    if city not in cities_info:
        cities_info[city] = [population, gold]
    else:
        cities_info[city][0] += population
        cities_info[city][1] += gold
    command = input()

new_command = input()
while new_command != 'End':
    current_command = new_command.split('=>')
    operation = current_command[0]
    if operation == 'Plunder':
        city, people, gold = current_command[1], int(current_command[2]), int(current_command[3])
        cities_info[city][0] -= people
        cities_info[city][1] -= gold
        print(f'{city} plundered! {gold} gold stolen, {people} citizens killed.')
        if cities_info[city][0] <= 0 or cities_info[city][1] <= 0:
            del cities_info[city]
            print(f'{city} has been wiped off the map!')

    elif operation == 'Prosper':
        city, gold = current_command[1], int(current_command[2])
        if gold > 0:
            cities_info[city][1] += gold
            print(f'{gold} gold added to the city treasury. {city} now has {cities_info[city][1]} gold.')
        else:
            print('Gold added cannot be a negative number!')
    new_command = input()

if cities_info:
    print(f'Ahoy, Captain! There are {len(cities_info)} wealthy settlements to go to:')
    for key, value in cities_info.items():
        print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
