SIZE = int(input())
matrix = [[0] * SIZE for _ in range(SIZE)]
N = int(input())

for _ in range(N):
    row, col = list(map(int, input().strip('()').split(', ')))
    matrix[row][col] = '*'

directions = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)

)

for row in range(SIZE):
    for col in range(SIZE):
        if matrix[row][col] == '*':
            continue
        for direction in directions:
            temp_row = row + direction[0]
            temp_col = col + direction[1]

            if not(0 <= temp_row < SIZE and 0 <= temp_col < SIZE):
                continue

            if matrix[temp_row][temp_col] == '*':
                matrix[row][col] += 1

for row in matrix:
    print(' '.join(str(x) for x in row))
