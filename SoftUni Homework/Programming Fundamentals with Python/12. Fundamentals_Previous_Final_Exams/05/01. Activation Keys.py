activation_key = input()
command = input()
while command != 'Generate':
    current_command = command.split('>>>')
    operation = current_command[0]
    if operation == 'Contains':
        substring = current_command[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print('Substring not found!')

    elif operation == 'Flip':
        case = current_command[1]
        start_index, end_index = int(current_command[2]), int(current_command[3])
        if case == 'Upper':
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper()\
                             + activation_key[end_index:]
        elif case == 'Lower':
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower()\
                             + activation_key[end_index:]
        print(activation_key)
    elif operation == 'Slice':
        start_index, end_index = int(current_command[1]), int(current_command[2])
        activation_key = activation_key.replace(activation_key[start_index:end_index], '')
        print(activation_key)

    command = input()

print(f'Your activation key is: {activation_key}')
