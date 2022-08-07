password = input()
command = input()
while command != 'Done':
    current_command = command.split()
    operation = current_command[0]
    if operation == 'TakeOdd':
        password = ''.join(password[i] for i in range(len(password)) if i % 2 != 0)
        print(password)
    elif operation == 'Cut':
        index, lenght = int(current_command[1]), int(current_command[2])
        substring = password[index:index + lenght]
        password = password.replace(substring, '', 1)
        print(password)
    elif operation == 'Substitute':
        substring, substitute = current_command[1], current_command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")
