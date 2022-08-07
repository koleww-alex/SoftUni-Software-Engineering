string = input()
new_string = ""
number = ""
temporary_string = ""
for i in range(len(string)):

    if len(number) > 0 and not string[i].isdigit():
        new_string += temporary_string.upper() * int(number)
        number = ""
        temporary_string = ""

    if string[i].isdigit():
        number += string[i]
        if len(string) - 1 == i:
            new_string += temporary_string.upper() * int(number)

    else:
        temporary_string += string[i]
        if len(string) - 1 == i:
            new_string += temporary_string.upper()

print(f"Unique symbols used: {len(set(new_string))}")
print(new_string)
