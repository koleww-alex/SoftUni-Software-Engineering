rows, cols = map(int, input().split(', '))
matrix = []

for row in range(rows):
    matrix.append(list(map(int, input().split(', '))))

total_sum = 0

for row in matrix:
    for col in row:
        total_sum += col

print(total_sum)
print(matrix)
