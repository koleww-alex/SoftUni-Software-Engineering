size = int(input())
matrix = [[x for x in input()] for _ in range(size)]
most_attacks_by_knight = 0
most_attacks_by_knight_coordinates = []
knights_removed = 0
directions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, -1),
    (2, 1),
    (1, -2),
    (1, 2),
)
while True:
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                current_knight_attacks = 0

                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    if 0 <= new_row < size and 0 <= new_col < size:
                        if matrix[new_row][new_col] == 'K':
                            current_knight_attacks += 1

                if current_knight_attacks > most_attacks_by_knight:
                    most_attacks_by_knight = current_knight_attacks
                    most_attacks_by_knight_coordinates = [row, col]

    if most_attacks_by_knight == 0:
        print(knights_removed)
        break
    matrix[most_attacks_by_knight_coordinates[0]][most_attacks_by_knight_coordinates[1]] = '0'
    most_attacks_by_knight = 0
    knights_removed += 1
