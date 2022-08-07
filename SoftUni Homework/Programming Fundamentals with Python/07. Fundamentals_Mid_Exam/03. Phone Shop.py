list_of_phones = input().split(", ")
command = input()

while command != "End":
    current_command = command.split(" - ")
    operation = current_command[0]

    if operation == "Add":
        phone = current_command[1]
        if phone not in list_of_phones:
            list_of_phones.append(phone)

    elif operation == "Remove":
        phone = current_command[1]
        if phone in list_of_phones:
            list_of_phones.remove(phone)

    elif operation == "Bonus phone":
        phones = current_command[1].split(":")
        old_phone = phones[0]
        new_phone = phones[1]
        if old_phone in list_of_phones:
            old_phone_index = list_of_phones.index(old_phone)
            list_of_phones.insert(old_phone_index + 1, new_phone)

    elif operation == "Last":
        phone = current_command[1]
        if phone in list_of_phones:
            list_of_phones.remove(phone)
            list_of_phones.append(phone)

    command = input()

print(", ".join(list_of_phones))
