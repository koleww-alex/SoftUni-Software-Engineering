size = 5
matrix = [[x for x in input().split()] for _ in range(size)]
player_position = []
shot_targets_pos = []
total_targets = 0
targets_shot = 0
for row in range(size):
    if 'A' in matrix[row]:
        col = matrix[row].index('A')
        player_position = [row, col]
        matrix[row][col] = '.'
    if 'x' in matrix[row]:
        total_targets += matrix[row].count('x')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

N = int(input())
for _ in range(N):
    command = input().split()

    if 'shoot' in command:
        position = command[1]
        row, col = player_position
        for _ in range(size):
            row += directions[position][0]
            col += directions[position][1]
            if 0 <= row < size and 0 <= col < size:
                if matrix[row][col] == 'x':
                    matrix[row][col] = '.'
                    targets_shot += 1
                    shot_targets_pos.append([row, col])
                    break

        if total_targets == targets_shot:
            print(f'Training completed! All {targets_shot} targets hit.')
            break
    else:
        position, steps = command[1], int(command[2])
        row, col = player_position[0] + (directions[position][0] * steps),\
                   player_position[1] + (directions[position][1] * steps)
        if 0 <= row < size and 0 <= col < size and matrix[row][col] == '.':
            player_position = [row, col]
if total_targets > targets_shot:
    print(f'Training not completed! {total_targets - len(shot_targets_pos)} targets left.')
for target in shot_targets_pos:
    print(target)
