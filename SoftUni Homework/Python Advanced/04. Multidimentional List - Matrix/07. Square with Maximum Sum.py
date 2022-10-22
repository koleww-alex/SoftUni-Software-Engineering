rows, cols = map(int, input().split(', '))
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
biggest_square = []
max_sum = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        square = [
            matrix[row][col], matrix[row][col + 1],
            matrix[row + 1][col], matrix[row + 1][col + 1],
        ]

        if sum(square) > max_sum:
            max_sum = sum(square)
            biggest_square = square

for i in range(len(biggest_square)):
    if i == 2:
        print()
    print(biggest_square[i], end=' ')
print()
print(max_sum)
