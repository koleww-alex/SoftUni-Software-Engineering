from collections import deque
size = int(input())
commands = deque(input().split())
matrix = [[x for x in input().split()] for _ in range(size)]
starting_position = []
flag = False
stepped_on_e = False
coals_left = False
coals_found = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 's':
            starting_position.append((row, col))
            flag = True
            break
    if flag:
        break

current_position = (starting_position[0][0], starting_position[0][1])

while commands:
    starting_row, starting_col = starting_position[0]
    starting_row, starting_col = int(starting_row), int(starting_col)
    command = commands.popleft()

    if command == 'left':
        if current_position[1] - 1 < 0:
            continue
        current_position = current_position[0], current_position[1] - 1
        if matrix[current_position[0]][current_position[1]] == 'e':
            stepped_on_e = True
            print(f'Game over! ({current_position[0]}, {current_position[1]})')
            break
        elif matrix[current_position[0]][current_position[1]] == 'c':
            matrix[current_position[0]][current_position[1]] = '*'
            coals_found += 1

    elif command == 'right':
        if current_position[1] + 1 > size - 1:
            continue
        current_position = current_position[0], current_position[1] + 1
        if matrix[current_position[0]][current_position[1]] == 'e':
            stepped_on_e = True
            print(f'Game over! ({current_position[0]}, {current_position[1]})')
            break
        elif matrix[current_position[0]][current_position[1]] == 'c':
            matrix[current_position[0]][current_position[1]] = '*'
            coals_found += 1

    elif command == 'up':
        if current_position[0] - 1 < 0:
            continue
        current_position = current_position[0] - 1, current_position[1]
        if matrix[current_position[0]][current_position[1]] == 'e':
            stepped_on_e = True
            print(f'Game over! ({current_position[0]}, {current_position[1]})')
            break
        elif matrix[current_position[0]][current_position[1]] == 'c':
            matrix[current_position[0]][current_position[1]] = '*'
            coals_found += 1

    elif command == 'down':
        if current_position[0] + 1 > size - 1:
            continue
        current_position = current_position[0] + 1, current_position[1]
        if matrix[current_position[0]][current_position[1]] == 'e':
            stepped_on_e = True
            print(f'Game over! ({current_position[0]}, {current_position[1]})')
            break
        elif matrix[current_position[0]][current_position[1]] == 'c':
            matrix[current_position[0]][current_position[1]] = '*'
            coals_found += 1

    coals_left = False
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'c':
                coals_left = True
                break
        if coals_left:
            break

    if not coals_left:
        print(f'You collected all coal! ({current_position[0]}, {current_position[1]})')
        break

if not commands and not stepped_on_e and coals_left:
    remaining_coals = 0
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'c':
                remaining_coals += 1

    print(f'{remaining_coals} pieces of coal left. ({current_position[0]}, {current_position[1]})')


