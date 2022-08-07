string = input()
command = input()
while command != 'Finish':
    current_command = command.split()
    operation = current_command[0]
    if operation == 'Replace':
        current_ch, new_ch = current_command[1], current_command[2]
        string = string.replace(current_ch, new_ch)
        print(string)
    elif operation == 'Cut':
        start_index, end_index = int(current_command[1]), int(current_command[2])
        if 0 <= start_index and end_index < len(string):
            string = string[:start_index] + string[end_index + 1:]
            print(string)
        else:
            print('Invalid indices!')
    elif operation == 'Make':
        upper_or_lower = current_command[1]
        if upper_or_lower == 'Lower':
            string = string.lower()
        elif upper_or_lower == 'Upper':
            string = string.upper()
        print(string)
    elif operation == 'Check':
        given_string = current_command[1]
        if given_string in string:
            print(f'Message contains {given_string}')
        else:
            print(f"Message doesn't contain {given_string}")

    elif operation == 'Sum':
        start_index, end_index = int(current_command[1]), int(current_command[2])
        if 0 <= start_index and end_index < len(string):
            ascii_sum = 0
            substring = string[start_index:end_index + 1]
            for ch in substring:
                ascii_sum += ord(ch)
            print(ascii_sum)
        else:
            print('Invalid indices!')

    command = input()
