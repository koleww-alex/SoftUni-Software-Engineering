total_presents = int(input())
size = int(input())
matrix = [[x for x in input().split()] for _ in range(size)]
santa_pos = []
total_nice_kids = 0
gifts_given = 0
for row in range(size):
    if 'S' in matrix[row]:
        col = matrix[row].index('S')
        santa_pos = [row, col]
    if 'V' in matrix[row]:
        total_nice_kids += matrix[row].count('V')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
command = input()
while command:
    if command == 'Christmas morning':
        break
    new_row, new_col = santa_pos[0] + directions[command][0], santa_pos[1] + directions[command][1]
    if 0 <= new_row < size and 0 <= new_col < size:
        row, col = santa_pos
        matrix[row][col] = '-'

        santa_pos = [new_row, new_col]
        if matrix[new_row][new_col] == 'V':
            total_presents -= 1
            gifts_given += 1

        elif matrix[new_row][new_col] == 'C':
            for direction in directions:
                row, col = new_row + directions[direction][0], new_col + directions[direction][1]
                if 0 <= row < size and 0 <= col < size and matrix[row][col] == 'X' or matrix[row][col] == 'V':
                    if total_presents > 0:
                        if matrix[row][col] == 'V':
                            gifts_given += 1
                        matrix[row][col] = '-'
                        total_presents -= 1
        matrix[new_row][new_col] = 'S'
    if total_presents <= 0:
        break
    command = input()

if total_presents <= 0 and total_nice_kids > gifts_given:
    print('Santa ran out of presents!')

for row in range(size):
    print(' '.join(matrix[row]))
if total_nice_kids == gifts_given:
    print(f'Good job, Santa! {gifts_given} happy nice kid/s.')

else:
    print(f'No presents for {total_nice_kids - gifts_given} nice kid/s.')
