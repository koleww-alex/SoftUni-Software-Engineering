rows, cols = map(int, input().split())
matrix = [[x for x in input().split()] for _ in range(rows)]
square_matrices_cnt = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            square_matrices_cnt += 1

print(square_matrices_cnt)
