from math import floor


def function(num_one, num_two, num_three, num_four):
    min_num_one = 0
    min_num_two = 0
    if abs(num_one) <= abs(num_three):
        min_num_one = num_one
    else:
        min_num_one = num_three

    if abs(num_two) <= abs(num_four):
        min_num_two = num_two
    else:
        min_num_two = num_four

    return f"({floor(min_num_one):.0f}, {floor(min_num_two):.0f})"


x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())

print(function(x1, x2, y1, y2))
