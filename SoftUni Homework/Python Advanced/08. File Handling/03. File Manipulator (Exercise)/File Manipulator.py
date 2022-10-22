from os import remove
while True:
    command = input().split('-')

    if command[0] == 'Create':
        file_name = command[1]
        file = open(file_name, 'w')
        file.close()
    elif command[0] == 'Add':
        file_name, content = command[1], command[2]
        with open(file_name, 'a') as file:
            file.write(content + '\n')

    elif command[0] == 'Replace':
        file_name, old_string, new_string = command[1], command[2], command[3]
        try:
            with open(file_name, 'r') as file:
                text = file.read()
                text = text.replace(old_string, new_string)

            with open(file_name, 'w') as file:
                file.write(text)

        except FileNotFoundError:
            print('An error occurred')

    elif command[0] == 'Delete':
        file_name = command[1]
        try:
            remove(file_name)
        except FileNotFoundError:
            print('An error occurred')
    else:
        break
