size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
indices = input().split()
list_of_bombs = []

for pair in indices:
    row, col = pair.split(',')
    row, col = int(row), int(col)

    if size <= 0:
        break

    if size == 1 and row == 0 and col == 0:
        matrix[row][col] = 0
        break
    if size == 1 and row != 0 and col != 0:
        break

    if col == 0:
        if row == 0:
            if matrix[row][col + 1] > 0 and (row, col) not in list_of_bombs:
                matrix[row][col + 1] -= matrix[row][col]

            if matrix[row + 1][col] > 0 and (row, col) not in list_of_bombs:
                matrix[row + 1][col] -= matrix[row][col]

            if matrix[row + 1][col + 1] > 0 and (row, col) not in list_of_bombs:
                matrix[row + 1][col + 1] -= matrix[row][col]

            matrix[row][col] = 0

        elif row == size - 1:
            if matrix[row][col + 1] > 0 and (row, col) not in list_of_bombs:
                matrix[row][col + 1] -= matrix[row][col]

            if matrix[row - 1][col] > 0 and (row, col) not in list_of_bombs:
                matrix[row - 1][col] -= matrix[row][col]

            if matrix[row - 1][col + 1] > 0 and (row, col) not in list_of_bombs:
                matrix[row - 1][col + 1] -= matrix[row][col]

            matrix[row][col] = 0
        else:
            if matrix[row][col + 1] > 0 and (row, col) not in list_of_bombs:
                matrix[row][col + 1] -= matrix[row][col]

            if matrix[row - 1][col] > 0 and (row, col) not in list_of_bombs:
                matrix[row - 1][col] -= matrix[row][col]

            if matrix[row - 1][col + 1] > 0 and (row, col) not in list_of_bombs:
                matrix[row - 1][col + 1] -= matrix[row][col]

            if matrix[row + 1][col] > 0 and (row, col) not in list_of_bombs:
                matrix[row + 1][col] -= matrix[row][col]

            if matrix[row + 1][col + 1] > 0 and (row, col) not in list_of_bombs:
                matrix[row + 1][col + 1] -= matrix[row][col]

            matrix[row][col] = 0

    elif col == size - 1:

        if row == 0:
            if matrix[row][col - 1] > 0 and (row, col) not in list_of_bombs:
                matrix[row][col - 1] -= matrix[row][col]

            if matrix[row + 1][col] > 0 and (row, col) not in list_of_bombs:
                matrix[row + 1][col] -= matrix[row][col]

            if matrix[row + 1][col - 1] > 0 and (row, col) not in list_of_bombs:
                matrix[row + 1][col - 1] -= matrix[row][col]

            matrix[row][col] = 0

        elif row == size - 1:
            if matrix[row][col - 1] > 0 and (row, col) not in list_of_bombs:
                matrix[row][col - 1] -= matrix[row][col]

            if matrix[row - 1][col] > 0 and (row, col) not in list_of_bombs:
                matrix[row - 1][col] -= matrix[row][col]

            if matrix[row - 1][col - 1] > 0 and (row, col) not in list_of_bombs:
                matrix[row - 1][col - 1] -= matrix[row][col]

            matrix[row][col] = 0

        else:
            if matrix[row][col - 1] > 0 and (row, col) not in list_of_bombs:
                matrix[row][col - 1] -= matrix[row][col]

            if matrix[row - 1][col] > 0 and (row, col) not in list_of_bombs:
                matrix[row - 1][col] -= matrix[row][col]

            if matrix[row - 1][col - 1] > 0 and (row, col) not in list_of_bombs:
                matrix[row - 1][col - 1] -= matrix[row][col]

            if matrix[row + 1][col] > 0 and (row, col) not in list_of_bombs:
                matrix[row + 1][col] -= matrix[row][col]

            if matrix[row + 1][col - 1] > 0 and (row, col) not in list_of_bombs:
                matrix[row + 1][col - 1] -= matrix[row][col]

            matrix[row][col] = 0

    else:
        if matrix[row][col - 1] > 0 and (row, col) not in list_of_bombs:
            matrix[row][col - 1] -= matrix[row][col]

        if matrix[row][col + 1] > 0 and (row, col) not in list_of_bombs:
            matrix[row][col + 1] -= matrix[row][col]

        if matrix[row - 1][col] > 0 and (row, col) not in list_of_bombs:
            matrix[row - 1][col] -= matrix[row][col]

        if matrix[row - 1][col - 1] > 0 and (row, col) not in list_of_bombs:
            matrix[row - 1][col - 1] -= matrix[row][col]

        if matrix[row - 1][col + 1] > 0 and (row, col) not in list_of_bombs:
            matrix[row - 1][col + 1] -= matrix[row][col]

        if matrix[row + 1][col] > 0 and (row, col) not in list_of_bombs:
            matrix[row + 1][col] -= matrix[row][col]

        if matrix[row + 1][col - 1] > 0 and (row, col) not in list_of_bombs:
            matrix[row + 1][col - 1] -= matrix[row][col]

        if matrix[row + 1][col + 1] > 0 and (row, col) not in list_of_bombs:
            matrix[row + 1][col + 1] -= matrix[row][col]

        matrix[row][col] = 0

matrix_positive_cells_sum = 0
positive_cells_cnt = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] > 0:
            matrix_positive_cells_sum += matrix[row][col]
            positive_cells_cnt += 1

print(f'Alive cells: {positive_cells_cnt}')
print(f'Sum: {matrix_positive_cells_sum}')

for row in range(size):
    for col in range(size):
        print(matrix[row][col], end=' ')
    if row < size - 1:
        print()
