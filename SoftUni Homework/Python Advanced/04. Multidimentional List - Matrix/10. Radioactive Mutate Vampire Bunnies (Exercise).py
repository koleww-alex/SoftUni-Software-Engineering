rows, cols = tuple(map(int, input().split()))
matrix = [[col for col in list(input())] for row in range(rows)]
commands = list(input())
winner = False
reached = False
positions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}
player_current_position = ()
bunny_starting_position = ()
bunnies_current_positions = []
for row in range(rows):
    if 'P' in matrix[row]:
        player_current_position = row, matrix[row].index('P')
        matrix[row][matrix[row].index('P')] = '.'

    elif 'B' in matrix[row]:
        bunny_starting_position = row, matrix[row].index('B')

for command in commands:
    matrix[player_current_position[0]][player_current_position[1]] = '.'
    player_row, player_col = player_current_position[0] + positions[command][0], \
                             player_current_position[1] + positions[command][1]
    if 0 <= player_row < rows and 0 <= player_col < cols:
        player_current_position = player_row, player_col
        if matrix[player_row][player_col] == '.':
            matrix[player_row][player_col] = 'P'
        else:
            reached = True
    else:
        winner = True

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'B':
                bunnies_current_positions.append(row)
                bunnies_current_positions.append(col)

    for i in range(0, len(bunnies_current_positions), 2):
        bunny_row, bunny_col = bunnies_current_positions[i], bunnies_current_positions[i + 1]
        for position in positions:
            if 0 <= bunny_row + positions[position][0] < rows and 0 <= bunny_col + positions[position][1] < cols:
                if matrix[bunny_row + positions[position][0]][bunny_col + positions[position][1]] == 'P' and not winner:
                    reached = True
                    matrix[bunny_row + positions[position][0]][bunny_col + positions[position][1]] = 'B'

                matrix[bunny_row + positions[position][0]][bunny_col + positions[position][1]] = \
                    matrix[bunny_row + positions[position][0]][bunny_col + positions[position][1]].replace('.', 'B')

    if reached:
        for row in range(rows):
            for col in range(cols):
                print(matrix[row][col], end='')
            print()
        print(f'dead: {player_current_position[0]} {player_current_position[1]}')
        break

    if winner:
        for row in range(rows):
            for col in range(cols):
                print(matrix[row][col], end='')
            print()
        print(f'won: {player_current_position[0]} {player_current_position[1]}')
        break
