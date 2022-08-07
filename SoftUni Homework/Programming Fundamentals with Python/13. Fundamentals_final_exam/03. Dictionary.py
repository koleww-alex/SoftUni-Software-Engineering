notebook = {}
teacher_words = []
info = input().split(" | ")
for element in info:
    key, value = element.split(": ")
    if key not in notebook:
        notebook[key] = [value]
    else:
        notebook[key].append(value)

while True:
    command = input()
    if command == 'Test':
        for word in teacher_words:
            if word in notebook:
                print(f"{word}:")
                for value in notebook[word]:
                    print(f"-{value}")
        break
    elif command == 'Hand Over':
        print(" ".join(notebook))
        break

    current_command = command.split(" | ")
    for word in current_command:
        teacher_words.append(word)
