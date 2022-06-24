initial_health = 100
initial_bitcoins = 0
dungeon = input().split("|")
room_cnt = 0
you_died = False

for element in dungeon:
    element = element.split()
    room_cnt += 1
    operation = element[0]
    value = int(element[1])

    if operation == "potion":
        max_value = 100 - initial_health
        initial_health += value
        if initial_health > 100:
            initial_health = 100
            value = max_value
        print(f"You healed for {value} hp.")
        print(f"Current health: {initial_health} hp.")

    elif operation == "chest":
        print(f"You found {value} bitcoins.")
        initial_bitcoins += value

    else:
        current_monster = operation
        initial_health -= value
        if initial_health > 0:
            print(f"You slayed {current_monster}.")
        else:
            print(f"You died! Killed by {current_monster}.")
            you_died = True
            break

if you_died:
    print(f"Best room: {room_cnt}")

else:
    print(f"You've made it!\n"
          f"Bitcoins: {initial_bitcoins}\n"
          f"Health: {initial_health}")
