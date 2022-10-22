rows, cols = list(map(int, input().split(', ')))
matrix = [input().split() for row in range(rows)]
my_pos = []
total_items = 0
merry_christmas = False
for row in range(rows):
    if 'Y' in matrix[row]:
        my_pos = [row, matrix[row].index('Y')]
        matrix[row][matrix[row].index('Y')] = 'x'
    if 'D' in matrix[row]:
        total_items += matrix[row].count('D')
    if 'G' in matrix[row]:
        total_items += matrix[row].count('G')
    if 'C' in matrix[row]:
        total_items += matrix[row].count('C')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

collected_items = {
    'Christmas decorations': 0,
    'Gifts': 0,
    'Cookies': 0,
}

command = input().split('-')

while 'End' not in command:
    direction, steps = command
    for _ in range(int(steps)):
        row, col = my_pos
        matrix[row][col] = 'x'
        row, col = row + directions[direction][0], col + directions[direction][1]

        if not (0 <= row < rows and 0 <= col < cols):
            if direction == 'up':
                row = rows - 1
            elif direction == 'down':
                row = 0
            elif direction == 'left':
                col = cols - 1
            elif direction == 'right':
                col = 0

        if matrix[row][col] == 'D':
            collected_items['Christmas decorations'] += 1

        elif matrix[row][col] == 'G':
            collected_items['Gifts'] += 1

        elif matrix[row][col] == 'C':
            collected_items['Cookies'] += 1

        matrix[row][col] = 'Y'
        my_pos = [row, col]

        if sum(collected_items.values()) == total_items:
            print('Merry Christmas!')
            merry_christmas = True
            break
    if merry_christmas:
        break
    command = input().split('-')

print(f"You've collected:")
for key, val in collected_items.items():
    print(f'- {val} {key}')

for row in matrix:
    print(' '.join(row))
