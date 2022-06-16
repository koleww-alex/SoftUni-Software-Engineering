def ascii_printer(start, end):
    for i in range(start + 1, end):
        list_of_elements.append(chr(i))

    elements = " ".join(list_of_elements)
    return elements


list_of_elements = []
starting_point = ord(input())
ending_point = ord(input())

print(ascii_printer(starting_point, ending_point))
