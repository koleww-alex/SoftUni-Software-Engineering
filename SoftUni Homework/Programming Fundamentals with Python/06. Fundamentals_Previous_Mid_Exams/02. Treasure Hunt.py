initial_loot = input().split("|")
command = input()
is_chest_empty = False
total_ch = 0
while command != "Yohoho!":
    current_command = command.split()
    operation = current_command[0]

    if operation == "Loot":
        for i in range(len(current_command)):
            if current_command[i] not in initial_loot and i != 0:
                initial_loot.insert(0, current_command[i])

    elif operation == "Drop":
        index = int(current_command[1])

        if 0 <= index < len(initial_loot):
            item = initial_loot[index]
            initial_loot.insert(len(initial_loot), item)
            initial_loot.pop(index)

    elif operation == "Steal":
        count = int(current_command[1])

        if count >= len(initial_loot):
            print(", ".join(initial_loot))
            is_chest_empty = True
        else:
            print(", ".join(initial_loot[len(initial_loot) - count:]))
            del initial_loot[len(initial_loot) - count:]

    command = input()

for _ in "".join(initial_loot):
    total_ch += 1

average_gain = total_ch / len(initial_loot)

if is_chest_empty:
    print("Failed treasure hunt.")
else:
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
