number_juniors = int(input())
number_seniors = int(input())
type_terrain = input()

price_juniors = 0
price_seniors = 0
discount = 0

if type_terrain == "trail":
    price_juniors = number_juniors * 5.50
    price_seniors = number_seniors * 7

elif type_terrain == "cross-country":
    price_juniors = number_juniors * 8
    price_seniors = number_seniors * 9.50
    if number_juniors + number_seniors >= 50:
        discount = 0.25
elif type_terrain == "downhill":
    price_juniors = number_juniors * 12.25
    price_seniors = number_seniors * 13.75

else:
    price_juniors = number_juniors * 20
    price_seniors = number_seniors * 21.50

total_price = price_juniors + price_seniors
total_price -= total_price * discount
expenses = total_price * 0.05

gifted_sum = total_price - expenses

print(f"{gifted_sum:.2f}")
