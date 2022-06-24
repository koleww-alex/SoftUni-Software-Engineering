journal = input().split(", ")
command = input()


while command != "Craft!":
    current_command = command.split(" - ")
    operation = current_command[0]

    if operation == "Collect":
        item = current_command[1]
        if item not in journal:
            journal.append(item)

    elif operation == "Drop":
        item = current_command[1]
        if item in journal:
            journal.remove(item)

    elif operation == "Combine Items":
        items = current_command[1].split(":")
        old_item = items[0]
        new_item = items[1]
        old_item_index = 0
        for i in range(len(journal)):
            if journal[i] == old_item:
                old_item_index = i
                break
        if old_item in journal:
            journal.insert(old_item_index + 1, new_item)

    elif operation == "Renew":
        item = current_command[1]
        if item in journal:
            journal.insert(len(journal), item)
            journal.remove(item)

    command = input()

print(", ".join(journal))
