def get_magic_triangle(size: int):
    triangle = [[1], [1, 1]]
    temp_row = [1, 1]
    for _ in range(size - 2):
        row = [1]
        for i in range(len(temp_row) - 1):
            row.append(temp_row[i] + temp_row[i + 1])

        row.append(1)
        temp_row = row
        triangle.append(row)

    return triangle


