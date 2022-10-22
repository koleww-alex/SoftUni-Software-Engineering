size = int(input())
matrix = [[x for x in input().split()] for _ in range(size)]
alice_position = []
tea_bags = 0
for row in range(size):
    if 'A' in matrix[row]:
        col = matrix[row].index('A')
        alice_position = [row, col]
        matrix[row][col] = '*'
        break

positions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

while True:
    if tea_bags >= 10:
        break
    command = input()
    row, col = alice_position
    new_row, new_col = row + positions[command][0], col + positions[command][1]
    if 0 <= new_row < size and 0 <= new_col < size:

        if matrix[new_row][new_col] == 'R':
            matrix[new_row][new_col] = '*'
            print("Alice didn't make it to the tea party.")
            break

        if matrix[new_row][new_col] != '.' and matrix[new_row][new_col] != '*':
            tea_bags += int(matrix[new_row][new_col])
        matrix[new_row][new_col] = '*'
        alice_position = [new_row, new_col]

    else:
        print("Alice didn't make it to the tea party.")
        break

if tea_bags >= 10:
    print('She did it! She went to the party.')

print(*[' '.join(row) for row in matrix], sep='\n')
