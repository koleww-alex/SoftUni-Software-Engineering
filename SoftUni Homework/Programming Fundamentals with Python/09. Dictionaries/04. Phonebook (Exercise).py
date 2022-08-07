command = input()
phone_dict = {}
while "-" in command:
    phone_number = command.split("-")
    name, number = phone_number

    phone_dict[name] = number

    command = input()

number_of_iterations = int(command)

for _ in range(number_of_iterations):
    name = input()

    if name not in phone_dict:  # not in phone_dict.keys():
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phone_dict[name]}")
