n = int(input())
for _ in range(n):
    text = input()
    name = ""
    age = ""

    for i in range(len(text)):
        if text[i] == "@":
            for index in range(i + 1, len(text)):
                if text[index] == "|":
                    break
                name += text[index]

    for i in range(len(text)):
        if text[i] == "#":
            for index in range(i + 1, len(text)):
                if text[index] == "*":
                    break
                age += text[index]

    print(f"{name} is {int(age)} years old.")
