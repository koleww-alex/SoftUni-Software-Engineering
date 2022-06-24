current_version = list(map(int, input().split(".")))
current_version[-1] += 1

for number in range(len(current_version) - 1, -1, -1):
    if current_version[number] > 9:
        current_version[number] = 0
        current_version[number - 1] += 1

    elif current_version[number - 1] > 9:
        current_version[number - 1] = 0
        current_version[0] += 1

print(".".join(str(number) for number in current_version))

# print(".".join(list(map(str, current_version))))
