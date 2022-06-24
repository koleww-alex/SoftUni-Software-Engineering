list_of_targets = list(map(int, input().split()))
command = input()
targets_shot = 0
while command != "End":
    current_index = int(command)
    is_valid = True if 0 <= current_index < len(list_of_targets) else False
    if is_valid:
        for i in range(len(list_of_targets)):
            if i != current_index and list_of_targets[i] != -1:
                if list_of_targets[i] > list_of_targets[current_index]:
                    list_of_targets[i] -= list_of_targets[current_index]
                elif list_of_targets[i] <= list_of_targets[current_index]:
                    list_of_targets[i] += list_of_targets[current_index]

        list_of_targets[current_index] = -1
        targets_shot += 1

    command = input()

print(f"Shot targets: {targets_shot} -> {' '.join(str(num) for num in list_of_targets)}")
