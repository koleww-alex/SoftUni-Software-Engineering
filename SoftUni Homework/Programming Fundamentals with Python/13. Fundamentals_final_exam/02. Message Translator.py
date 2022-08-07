import re
number_of_iterations = int(input())
pattern = r'![A-Z][a-z]{2,}!:\[[A-Za-z]{8,}\]'
for _ in range(number_of_iterations):
    string = input()
    ascii_values = []
    match = re.search(pattern, string)
    if match:
        text = match.group().split(':')
        command, message = text[0], text[1]
        command = command.replace('!', '')
        message = message.replace('[', '')
        message = message.replace(']', '')
        for ch in message:
            ascii_values.append(str(ord(ch)))
        print(f'{command}: {" ".join(ascii_values)}')

    else:
        print('The message is invalid')
