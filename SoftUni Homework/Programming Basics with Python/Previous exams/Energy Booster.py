fruit = input()
set_size = input()
number_of_sets = int(input())
set_price = 0

if fruit == "Watermelon":
    if set_size == "big":
        set_price = 5 * 28.70
    else:
        set_price = 2 * 56

elif fruit == "Mango":
    if set_size == "big":
        set_price = 5 * 19.60
    else:
        set_price = 2 * 36.66

elif fruit == "Pineapple":
    if set_size == "big":
        set_price = 5 * 24.80
    else:
        set_price = 2 * 42.10

else:
    if set_size == "big":
        set_price = 5 * 15.20
    else:
        set_price = 2 * 20

total_price = set_price * number_of_sets

if 400 <= total_price <= 1000:
    total_price -= total_price * 0.15

elif total_price > 1000:
    total_price = total_price / 2

print(f"{total_price:.2f} lv.")
