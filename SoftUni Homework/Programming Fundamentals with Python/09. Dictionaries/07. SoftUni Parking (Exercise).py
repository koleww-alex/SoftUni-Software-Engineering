from collections import defaultdict
number_of_commands = int(input())
data_base = defaultdict(str)

for _ in range(number_of_commands):
    current_command = input().split()
    operation = current_command[0]
    username = current_command[1]

    if operation == "register":
        license_plate = current_command[2]
        if username not in data_base:
            data_base[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    else:
        if username not in data_base:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            data_base.pop(username)

for username, value in data_base.items():
    print(f"{username} => {value}")
