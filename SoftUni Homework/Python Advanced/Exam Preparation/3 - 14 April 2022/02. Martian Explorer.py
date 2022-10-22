SIZE = 6
matrix = [input().split() for _ in range(SIZE)]
rover_commands = input().split(', ')
rover_pos = []
for row in range(SIZE):
    if 'E' in matrix[row]:
        rover_pos = [row, matrix[row].index('E')]
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
deposits = {
    'W': ['Water', 0],
    'M': ['Metal', 0],
    'C': ['Concrete', 0],
}

for command in rover_commands:
    rover_row, rover_col = rover_pos[0] + directions[command][0], rover_pos[1] + directions[command][1]
    if not (0 <= rover_row < SIZE and 0 <= rover_col < SIZE):
        if command == 'up':
            rover_row = SIZE - 1
        elif command == 'down':
            rover_row = 0
        elif command == 'left':
            rover_col = SIZE - 1
        elif command == 'right':
            rover_col = 0
    rover_pos = [rover_row, rover_col]
    pos = matrix[rover_row][rover_col]
    if pos == '-':
        continue
    if pos == 'R':
        print(f'Rover got broken at ({rover_row}, {rover_col})')
        break

    deposits[pos][1] += 1
    print(f'{deposits[pos][0]} deposit found at ({rover_row}, {rover_col})')

if deposits['W'][1] and deposits['M'][1] and deposits['C'][1]:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
