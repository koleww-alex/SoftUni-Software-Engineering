def take_odd(password: str):
    password = ''.join(password[i] for i in range(len(password)) if i % 2 != 0)
    print(password)
    return password


def cut(index: int, lenght: int, password: str):
    substring = password[index:index + lenght]
    password = password.replace(substring, '', 1)
    print(password)
    return password


def substitute_func(substring: str, substitute: str, password: str):
    if substring in password:
        password = password.replace(substring, substitute)
        print(password)
    else:
        print("Nothing to replace!")
    return password


password = input()
command = input()

while command != 'Done':
    current_command = command.split()
    operation = current_command[0]
    if operation == 'TakeOdd':
        password = take_odd(password)
    elif operation == 'Cut':
        index, lenght = int(current_command[1]), int(current_command[2])
        password = cut(index, lenght, password)
    elif operation == 'Substitute':
        substring, substitute = current_command[1], current_command[2]
        password = substitute_func(substring, substitute, password)

    command = input()

print(f"Your password is: {password}")
