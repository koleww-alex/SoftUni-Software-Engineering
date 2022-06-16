to_do_list = []
command = input()

while command != "End":
    current_command = command.split("-")

    importance = current_command[0]
    note = current_command[1]
    to_do_list.append((importance, note))
    command = input()

sorted_list = [sorted_task[1] for sorted_task in sorted(to_do_list)]

print(sorted_list)
