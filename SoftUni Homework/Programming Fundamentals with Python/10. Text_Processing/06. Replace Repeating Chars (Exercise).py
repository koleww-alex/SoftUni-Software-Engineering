string = input()
index = 0
new_string = ""
i = 0
time_to_break = False
for _ in range(len(string)):
    if time_to_break:
        break
    new_string += string[i]
    while new_string[index] == string[i]:
        i += 1
        if i >= len(string):
            time_to_break = True
            break
        continue
    index += 1
print(new_string)
