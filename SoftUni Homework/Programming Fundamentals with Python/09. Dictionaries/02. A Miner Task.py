my_dictionary = {}
while True:
    command = input()
    if command == "stop":
        break

    key, value = command, int(input())

    if key.lower() not in my_dictionary:
        my_dictionary[key] = 0
    my_dictionary[key] += value

print("\n".join(f"{key} -> {value}" for key, value in my_dictionary.items()))
