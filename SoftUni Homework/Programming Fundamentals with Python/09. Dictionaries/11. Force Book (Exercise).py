data_base = {}
while True:
    command = input()

    if "|" in command:
        current_command = command.split(" | ")
        force_side, force_user = current_command
        present = False
        for value in data_base.values():
            if force_user in value:
                present = True
                break
        if not present:
            if force_side not in data_base.keys():
                data_base[force_side] = [force_user]
            else:
                data_base[force_side].append(force_user)

    elif "->" in command:
        current_command = command.split(" -> ")
        force_user, force_side = current_command
        present = False

        for key, value in data_base.items():
            if force_user in value:
                data_base[key].remove(force_user)
                break

        if force_side not in data_base.keys():
            data_base[force_side] = [force_user]
        else:
            data_base[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    else:
        break

for force_side, list_of_users in data_base.items():
    if len(list_of_users) > 0:
        print(f"Side: {force_side}, Members: {len(list_of_users)}")
        print("\n".join(f"! {name}" for name in list_of_users))
