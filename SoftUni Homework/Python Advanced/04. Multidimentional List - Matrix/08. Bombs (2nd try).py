size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
bombs = [int(x) for x in input().replace(' ', ',').split(',')]
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
    'top_left_diagonal': (-1, -1),
    'top_right_diagonal': (-1, 1),
    'bottom_left_diagonal': (1, -1),
    'bottom_right_diagonal': (1, 1),
}
for i in range(0, len(bombs), 2):
    bomb_row, bomb_col = int(bombs[i]), int(bombs[i + 1])
    bomb_power = matrix[bomb_row][bomb_col]
    if bomb_power <= 0:
        continue
    matrix[bomb_row][bomb_col] = 0
    for direction in directions:
        r, c = bomb_row + directions[direction][0], bomb_col + directions[direction][1]
        if 0 <= r < size and 0 <= c < size:
            if matrix[r][c] > 0:
                matrix[r][c] -= bomb_power
sum_of_cells = 0
alive_cells = 0
for row in range(size):
    for col in range(size):
        if matrix[row][col] > 0:
            alive_cells += 1
            sum_of_cells += matrix[row][col]
print(f'Alive cells: {alive_cells}')
print(f'Sum: {sum_of_cells}')
[print(*matrix[row]) for row in range(size)]
