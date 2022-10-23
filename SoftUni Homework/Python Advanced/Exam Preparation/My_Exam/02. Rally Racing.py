SIZE = int(input())
race_car_num = input()
race_car_coordinates = [0, 0]
matrix = [input().split() for _ in range(SIZE)]
tunnels_coordinates = []
total_kilometers = 0
finished = False
for row in range(SIZE):
    if 'T' in matrix[row]:
        tunnels_coordinates.append([row, matrix[row].index('T')])

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command = input()
while command != 'End':
    row, col = race_car_coordinates
    n_row, n_col = row + directions[command][0], col + directions[command][1]
    total_kilometers += 10
    pos = matrix[n_row][n_col]
    if pos == 'F':
        finished = True
        print(f'Racing car {race_car_num} finished the stage!')
        race_car_coordinates = [n_row, n_col]
        break

    elif pos == 'T':
        total_kilometers += 20
        matrix[n_row][n_col] = '.'
        first_tunnel, second_tunnel = tunnels_coordinates[0], tunnels_coordinates[1]

        if [n_row, n_col] == first_tunnel:
            n_row, n_col = second_tunnel
        else:
            n_row, n_col = first_tunnel

        matrix[n_row][n_col] = '.'

    race_car_coordinates = [n_row, n_col]
    command = input()

if not finished:
    print(f'Racing car {race_car_num} DNF.')

print(f'Distance covered {total_kilometers} km.')

row, col = race_car_coordinates
matrix[row][col] = 'C'
for row in matrix:
    print(''.join(row))
