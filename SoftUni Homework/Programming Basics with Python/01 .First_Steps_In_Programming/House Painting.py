x = float(input())
y = float(input())
h = float(input())
liter_green_paint = 3.4
liter_red_paint = 4.3
front_wall = x * x - (1.2 * 2)
back_wall = x * x
right_side_wall = x * y - (1.5 * 1.5)
left_side_wall = x * y - (1.5 * 1.5)
roof_sides = 2 * (x * y)
roof_front_and_back = 2 * (x * h / 2)
size_base = front_wall + back_wall + right_side_wall + left_side_wall
size_roof = roof_sides + roof_front_and_back
litres_green_paint_house = size_base / liter_green_paint
litres_red_paint_house = size_roof / liter_red_paint
print(f"{litres_green_paint_house:.2f}")
print(f"{litres_red_paint_house:.2f}")
