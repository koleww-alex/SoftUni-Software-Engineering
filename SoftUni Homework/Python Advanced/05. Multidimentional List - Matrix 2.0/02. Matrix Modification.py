size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
while True:
    command = input().split()
    if 'END' in command:
        [print(*matrix[row]) for row in range(size)]
        break

    operation, row, col, number = command
    if 0 <= int(row) < size and 0 <= int(col) < size:
        if operation == 'Add':
            matrix[int(row)][int(col)] += int(number)
        elif operation == 'Subtract':
            matrix[int(row)][int(col)] -= int(number)
    else:
        print('Invalid coordinates')
