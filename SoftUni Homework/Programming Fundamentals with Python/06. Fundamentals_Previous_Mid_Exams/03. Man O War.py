pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_health_capacity = int(input())
command = input()
someone_lost = False
while command != "Retire":
    current_command = command.split()
    operation = current_command[0]

    if operation == "Fire":
        index = int(current_command[1])
        damage = int(current_command[2])

        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                someone_lost = True
                break

    elif operation == "Defend":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        damage = int(current_command[3])
        if 0 <= start_index and end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    someone_lost = True
                    break
            if someone_lost:
                break

    elif operation == "Repair":
        index = int(current_command[1])
        health = int(current_command[2])

        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health_capacity:
                pirate_ship[index] = max_health_capacity

    elif operation == "Status":
        repair_cnt = 0
        for i in range(len(pirate_ship)):
            if pirate_ship[i] < max_health_capacity * 0.2:
                repair_cnt += 1
        print(f"{repair_cnt} sections need repair.")

    command = input()

if not someone_lost:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
