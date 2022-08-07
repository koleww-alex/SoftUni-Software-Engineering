my_dict = {}
submissions = {}
command = input()
while "exam finished" not in command:
    current_command = command.split("-")
    if len(current_command) > 2:
        username = current_command[0]
        language = current_command[1]
        points = int(current_command[2])
        if username not in my_dict:
            my_dict[username] = [language, points]

        if int(my_dict[username][1]) < points and my_dict[username][0] == language:
            my_dict[username][1] = points

        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
    else:
        banned_name = current_command[0]
        for key in my_dict:
            if key == banned_name:
                my_dict[key].append("banned")
    command = input()

print("Results:")
print("\n".join(f"{key} | {value[1]}" for key, value in my_dict.items() if "banned" not in value))
print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")
