from sys import maxsize

rows, cols = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
biggest_matrix = []
biggest_matrix_sum = -maxsize

for row in range(rows - 2):
    for col in range(cols - 2):
        current_matrix = [
            [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
            [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
            [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        ]

        current_matrix_sum = sum(map(sum, current_matrix))
        if current_matrix_sum > biggest_matrix_sum:
            biggest_matrix = current_matrix
            biggest_matrix_sum = current_matrix_sum

print(f'Sum = {biggest_matrix_sum}')

for row in range(len(biggest_matrix)):
    for col in range(len(biggest_matrix)):
        print(biggest_matrix[row][col], end=' ')

    if row < len(biggest_matrix) - 1:
        print()
