rows, cols = map(int, input().split())
matrix = []

for row in range(rows):
    string = ''
    for col in range(cols):
        string += chr(97 + row) + chr(97 + row + col) + chr(97 + row)
        if col < cols - 1:
            string += ' '
    matrix.append(string.split())

for row in matrix:
    print(' '.join(row))
