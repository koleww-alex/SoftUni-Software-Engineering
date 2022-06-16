# цвете	Роза	Далия	Лале	Нарцис	Гладиола
# Цен лева	5	3.80	2.80	3	2.50

flower_type = input()
number_flowers = int(input())
budget = int(input())

price_per_flower = 0
percent_discount = 0
higher_percent_rate = 0
total_price = 0

if flower_type == "Roses":
    price_per_flower = 5
    if number_flowers > 80:
        percent_discount = 0.1

elif flower_type == "Dahlias":
    price_per_flower = 3.80
    if number_flowers > 90:
        percent_discount = 0.15

elif flower_type == "Tulips":
    price_per_flower = 2.80
    if number_flowers > 80:
        percent_discount = 0.15

elif flower_type == "Narcissus":
    price_per_flower = 3
    if number_flowers < 120:
        higher_percent_rate = 0.15

elif flower_type == "Gladiolus":
    price_per_flower = 2.50
    if number_flowers < 80:
        higher_percent_rate = 0.2
# raw price:
total_price = number_flowers * price_per_flower

# price with percent_discount and higher_percent_rate

total_price -= total_price * percent_discount
total_price += total_price * higher_percent_rate

if budget >= total_price:
    money_left = budget - total_price
    print(f"Hey, you have a great garden with {number_flowers} {flower_type} and {money_left:.2f} leva left.")
else:
    money_needed = total_price - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")
