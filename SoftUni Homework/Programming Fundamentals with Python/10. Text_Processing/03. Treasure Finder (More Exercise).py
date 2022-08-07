keys = input().split()
string = input()
while "find" not in string:
    updated_string = ""
    i = 0
    value = ""
    coordinates = ""
    for ch in string:
        if len(keys) == i:
            i = 0
        updated_string += chr(ord(ch) - int(keys[i]))
        i += 1

    for i in range(len(updated_string)):
        if updated_string[i] == "&":
            for index in range(i + 1, len(updated_string)):
                ch = updated_string[index]
                if ch == "&":
                    break
                value += ch
            break

    for i in range(len(updated_string)):
        if updated_string[i] == "<":
            for index in range(i + 1, len(updated_string)):
                ch = updated_string[index]
                if ch == ">":
                    break
                coordinates += ch
            break

    print(f"Found {value} at {coordinates}")
    string = input()
