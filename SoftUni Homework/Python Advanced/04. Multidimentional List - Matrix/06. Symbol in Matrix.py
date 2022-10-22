size = int(input())
matrix = [[x for x in list(input())] for _ in range(size)]
searched_chr = input()
flag = False

for row in range(size):
    for col in range(size):
        current_chr = matrix[row][col]
        if current_chr == searched_chr:
            flag = True
            print(f'({row}, {col})')
            break
    if flag:
        break

if not flag:
    print(f'{searched_chr} does not occur in the matrix')
