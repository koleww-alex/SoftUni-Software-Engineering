flower_type = input()
number_flowers = int(input())
budget = int(input())

price = 0
discount_percent = 0
higher_rate_percent = 0
price_per_flower = 0

if flower_type == "Roses":
    price_per_flower = 5
    if number_flowers > 80:
        discount_percent = 0.1
elif flower_type == "Dahlias":
    price_per_flower = 3.8
    if number_flowers > 90:
        discount_percent = 0.15
elif flower_type == "Tulips":
    price_per_flower = 2.80
    if number_flowers > 80:
        discount_percent = 0.15
elif flower_type == "Narcissus":
    price_per_flower = 3
    if number_flowers < 120:
        higher_rate_percent = 0.15
elif flower_type == "Gladiolus":
    price_per_flower = 2.50
    if number_flowers < 80:
        higher_rate_percent = 0.2

price = number_flowers * price_per_flower
price -= price * discount_percent
price += price * higher_rate_percent


if budget >= price:
    money_left = budget - price
    print(f"Hey, you have a great garden with {number_flowers} {flower_type} and {money_left:.2f} leva left.")
else:
    money_needed = price - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")
