from collections import deque

string = deque(input().split())
colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
colors_made = []

while len(string):
    if len(string) > 1:
        substring = string[0] + string[-1]
        reversed_substring = string[-1] + string[0]
    else:
        substring = string[0]
        reversed_substring = substring

    if substring in colors:
        colors_made.append(substring)
        if len(string) > 1:
            string.popleft()
            string.pop()
        else:
            string.pop()
    elif reversed_substring in colors:
        colors_made.append(reversed_substring)
        if len(string) > 1:
            string.popleft()
            string.pop()
        else:
            string.pop()

    else:
        if len(string) > 1:
            first_string, last_string = string.popleft(), string.pop()

            first_string = first_string[:len(first_string) - 1]
            last_string = last_string[:len(last_string) - 1]
            if first_string:
                string.insert(len(string) // 2, first_string)

            if last_string:
                string.insert(len(string) // 2, last_string)
        else:
            break

if 'red' not in colors_made or 'yellow' not in colors_made:
    if 'orange' in colors_made:
        colors_made.remove('orange')

if 'red' not in colors_made or 'blue' not in colors_made:
    if 'purple' in colors_made:
        colors_made.remove('purple')

if 'yellow' not in colors_made or 'blue' not in colors_made:
    if 'green' in colors_made:
        colors_made.remove('green')

print(colors_made)
