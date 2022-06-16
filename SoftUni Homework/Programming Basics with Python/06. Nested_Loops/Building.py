number_cols = int(input())
number_rows = int(input())

flat_number = 0
flat_name = ""

for col in range(number_cols, 0, -1):
    for rows in range(0, number_rows):
        flat_number = col * 10 + rows
        if col == number_cols:
            flat_name = "L"
        elif col % 2 == 0:
            flat_name = "O"
        else:
            flat_name = "A"
        print(f"{flat_name}{flat_number}", end=" ")
    print()

