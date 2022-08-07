from collections import defaultdict

info = defaultdict(list)
command = input()
while ":" in command:
    command = command.split(":")
    name, number, course = command[0], command[1], command[2]
    info[name] = [number, course]

    command = input()
searched_course = " ".join(command.split("_"))
print("\n".join(f"{key} - {value[0]}" for key, value in info.items() if searched_course in value[1]))

