rows, cols = map(int, input().split())
matrix = [[x for x in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    if 'END' in command:
        break

    if 'swap' in command and len(command) == 5:
        first_point, second_point = command[1:3], command[3:5]
        first_point_one, first_point_two = map(int, first_point)
        second_point_one, second_point_two = map(int, second_point)
        if 0 <= first_point_one <= len(matrix) and 0 <= first_point_two <= len(matrix) and\
                0 <= second_point_one <= len(matrix) and 0 <= second_point_two <= len(matrix):
            matrix[first_point_one][first_point_two], matrix[second_point_one][second_point_two] = \
                matrix[second_point_one][second_point_two], matrix[first_point_one][first_point_two]

            for row in matrix:
                print(' '.join(str(x) for x in row))
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
