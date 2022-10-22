SIZE = 7
players_names = input().split(', ')
turn = [[players_names[0], 501, 0], [players_names[1], 501, 0]]
matrix = [input().split() for _ in range(SIZE)]
directions = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
)

while True:
    row, col = list(map(int, input().strip('()').split(', ')))
    turn[0][2] += 1
    if not (0 <= row < SIZE and 0 <= col < SIZE):
        turn.append(turn.pop(0))
        continue

    position = matrix[row][col]
    if position == 'B':
        print(f'{turn[0][0]} won the game with {turn[0][2]} throws!')
        break

    elif position == 'D':
        score = 0
        for direction in directions:
            temp_row, temp_col = row, col
            for i in range(SIZE - 1):
                temp_row += direction[0]
                temp_col += direction[1]

                if not (0 <= temp_row < SIZE and 0 <= temp_col < SIZE):
                    break

                if matrix[temp_row][temp_col].isdigit():
                    score += int(matrix[temp_row][temp_col])

        turn[0][1] -= score * 2

    elif position == 'T':
        score = 0
        for direction in directions:
            temp_row, temp_col = row, col
            for i in range(SIZE - 1):
                temp_row += direction[0]
                temp_col += direction[1]

                if not (0 <= temp_row < SIZE and 0 <= temp_col < SIZE):
                    break

                if matrix[temp_row][temp_col].isdigit():
                    score += int(matrix[temp_row][temp_col])

        turn[0][1] -= score * 3

    else:
        turn[0][1] -= int(position)

    if turn[0][1] <= 0:
        print(f'{turn[0][0]} won the game with {turn[0][2]} throws!')
        break

    turn.append(turn.pop(0))
