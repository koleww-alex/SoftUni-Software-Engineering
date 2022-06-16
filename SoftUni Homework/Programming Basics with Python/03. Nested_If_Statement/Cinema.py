screen_type = input()
number_rows = int(input())
number_columns = int(input())
total_price = 0
total_seats = number_columns * number_rows

if screen_type == "Premiere":
    total_price = total_seats * 12
elif screen_type == "Normal":
    total_price = total_seats * 7.50
else:
    total_price = total_seats * 5

print(f"{total_price:.2f} leva")
