size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
matrix_diagonal_sum = 0

for i in range(size):
    matrix_diagonal_sum += matrix[i][i]

print(matrix_diagonal_sum)

# Different approach (same logic)

for row in range(size):
    for col in range(size):
        matrix_diagonal_sum += matrix[row][col]
        row += 1
        col += 1
    break

print(matrix_diagonal_sum)
