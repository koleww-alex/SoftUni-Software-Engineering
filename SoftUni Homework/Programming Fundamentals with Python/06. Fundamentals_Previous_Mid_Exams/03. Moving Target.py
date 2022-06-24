list_of_targets = list(map(int, input().split()))
command = input().split()
while "End" not in command:
    operation = command[0]

    if operation == "Shoot":
        index = int(command[1])
        power = int(command[2])

        is_valid = 0 <= index < len(list_of_targets)

        if is_valid:
            list_of_targets[index] -= power
            if list_of_targets[index] <= 0:
                list_of_targets.pop(index)

    elif operation == "Add":
        index = int(command[1])
        value = int(command[2])

        is_valid = 0 <= index < len(list_of_targets)

        if is_valid:
            list_of_targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif operation == "Strike":
        index = int(command[1])
        radius = int(command[2])
        start_index = index - radius
        end_index = index + radius

        if 0 <= start_index and end_index < len(list_of_targets):
            del list_of_targets[start_index:end_index + 1]
        else:
            print("Strike missed!")

    command = input().split()

print("|".join(str(num) for num in list_of_targets))
