SIZE = 8
matrix = [input().split() for _ in range(SIZE)]
all_queens_positions = []
king_pos = []
successful_queens = []
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
        if matrix[row][col] == 'Q':
            all_queens_positions.extend([row, col])
        elif matrix[row][col] == 'K':
            king_pos = [row, col]


for i in range(0, len(all_queens_positions), 2):
    row, col = all_queens_positions[i], all_queens_positions[i + 1]
    king_found = False
    for direction in directions:
        temp_row, temp_col = row, col
        for _ in range(SIZE - 1):
            temp_row += direction[0]
            temp_col += direction[1]

            if not(0 <= temp_row < SIZE and 0 <= temp_col < SIZE):
                break

            elif matrix[temp_row][temp_col] == 'Q':
                break

            elif matrix[temp_row][temp_col] == 'K':
                successful_queens.append([row, col])
                king_found = True
                break

        if king_found:
            break

if successful_queens:
    for queen in successful_queens:
        print(queen)
else:
    print('The king is safe!')
