from math import floor
SIZE = int(input())
matrix = [input().split() for _ in range(SIZE)]
player_pos = []
coins_collected = 0

for row in range(SIZE):
    if 'P' in matrix[row]:
        player_pos = [row, matrix[row].index('P')]

path = [player_pos]
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    row, col = player_pos
    command = input()

    temp_row, temp_col = row + directions[command][0], col + directions[command][1]

    if not (0 <= temp_row < SIZE and 0 <= temp_col < SIZE):
        if command == 'up':
            temp_row = SIZE - 1
        elif command == 'down':
            temp_row = 0
        elif command == 'left':
            temp_col = SIZE - 1
        elif command == 'right':
            temp_col = 0

    path.append([temp_row, temp_col])
    pos = matrix[temp_row][temp_col]

    if pos.isdigit():
        coins_collected += int(pos)
        matrix[temp_row][temp_col] = '.'

    elif pos == 'X':
        coins_collected = floor(coins_collected / 2)
        print(f"Game over! You've collected {coins_collected} coins.")
        break

    if coins_collected >= 100:
        print(f"You won! You've collected {coins_collected} coins.")
        break

    player_pos = [temp_row, temp_col]

print('Your path:')
for item in path:
    print(item)

