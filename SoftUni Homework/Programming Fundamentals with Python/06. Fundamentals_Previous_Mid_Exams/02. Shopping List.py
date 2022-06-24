shopping_list = input().split("!")
command = input()

while command != "Go Shopping!":
    current_command = command.split()
    operation = current_command[0]

    if operation == "Urgent":
        item = current_command[1]
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif operation == "Unnecessary":
        item = current_command[1]
        if item in shopping_list:
            shopping_list.remove(item)
    elif operation == "Correct":
        old_item = current_command[1]
        new_item = current_command[2]
        if old_item in shopping_list:
            for i in range(len(shopping_list)):
                if shopping_list[i] == old_item:
                    shopping_list[i] = new_item
                    break
    elif operation == "Rearrange":
        item = current_command[1]
        if item in shopping_list:
            shopping_list.remove(item)
            last_index = len(shopping_list)
            shopping_list.insert(last_index, item)

    command = input()

print(", ".join(shopping_list))
