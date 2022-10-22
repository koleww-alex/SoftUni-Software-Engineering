word = input()
SIZE = int(input())
matrix = [list(input()) for _ in range(SIZE)]
my_pos = []
for row in range(SIZE):
    if 'P' in matrix[row]:
        my_pos = [row, matrix[row].index('P')]
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

N = int(input())
for _ in range(N):
    side = input()
    row, col = my_pos

    temp_row, temp_col = row + directions[side][0], col + directions[side][1]

    if not(0 <= temp_row < SIZE and 0 <= temp_col < SIZE):
        if word:
            word = word[:-1]
        continue

    matrix[row][col] = '-'
    if matrix[temp_row][temp_col] != '-':
        word += matrix[temp_row][temp_col]

    matrix[temp_row][temp_col] = 'P'
    my_pos = [temp_row, temp_col]

print(word)
for row in matrix:
    print(''.join(row))
