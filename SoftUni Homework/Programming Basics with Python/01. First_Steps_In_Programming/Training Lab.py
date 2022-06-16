w = float(input())
h = float(input())
area = w * h
available_h = h - 1
workplace_one_line = available_h // 0.7
lines_on_area = w // 1.2
available_places = workplace_one_line * lines_on_area - 3
print(available_places)
