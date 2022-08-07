string = input()
strength = 0
new_string = ""
for i in range(len(string)):
    if string[i] == ">":
        strength += int(string[i + 1])
        new_string += string[i]
    elif string[i] != ">" and strength == 0:
        new_string += string[i]

    else:
        strength -= 1

print(new_string)
