SIZE = 6
matrix = [input().split() for _ in range(SIZE)]
s_row, s_col = input().strip('()').split(', ')
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
command = input().split(', ')

while 'Stop' not in command:
    operation, direction = command[0], command[1]
    s_row, s_col = int(s_row) + directions[direction][0], int(s_col) + directions[direction][1]

    if operation == 'Create':
        create_symbol = command[2]
        if matrix[s_row][s_col] == '.':
            matrix[s_row][s_col] = create_symbol

    elif operation == 'Read':
        if matrix[s_row][s_col] != '.':
            print(matrix[s_row][s_col])

    elif operation == 'Update':
        update_symbol = command[2]
        if matrix[s_row][s_col] != '.':
            matrix[s_row][s_col] = update_symbol

    elif operation == 'Delete':
        if matrix[s_row][s_col] != '.':
            matrix[s_row][s_col] = '.'

    command = input().split(', ')

for row in matrix:
    print(' '.join(row))
