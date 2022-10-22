size = int(input())
matrix = [[x for x in input().split()] for _ in range(size)]
bunny_coordinates = []
directions = {
    'up': (-1, 0),
    'left': (0, -1),
    'right': (0, 1),
    'down': (1, 0)
}
max_sum = 0
best_path = ''
best_path_coordinates = []
for row in range(size):
    if 'B' in matrix[row]:
        col = matrix[row].index('B')
        bunny_coordinates = [row, col]
        break

for direction in directions:
    temp_sum = 0
    current_path_coordinates = []
    row, col = bunny_coordinates

    for i in range(size):
        if direction == 'up':
            new_row, new_col = row + directions[direction][0] - i, col + directions[direction][1]
        elif direction == 'down':
            new_row, new_col = row + directions[direction][0] + i, col + directions[direction][1]

        elif direction == 'left':
            new_row, new_col = row + directions[direction][0], col + directions[direction][1] - i

        else:
            new_row, new_col = row + directions[direction][0], col + directions[direction][1] + i

        if 0 <= new_row < size and 0 <= new_col < size:
            if matrix[new_row][new_col] == 'X':
                if temp_sum >= max_sum:
                    max_sum = temp_sum
                    best_path = direction
                    best_path_coordinates = current_path_coordinates
                break
            else:
                temp_sum += int(matrix[new_row][new_col])
                current_path_coordinates.append([new_row, new_col])
        else:
            if temp_sum >= max_sum:
                max_sum = temp_sum
                best_path = direction
                best_path_coordinates = current_path_coordinates
                break
            else:
                break

print(best_path)
for path in best_path_coordinates:
    print(path)
print(max_sum)
