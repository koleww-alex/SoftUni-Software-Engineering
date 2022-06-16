budget = float(input())
number_nights = int(input())
price_per_night = float(input())
percent_expenses = int(input()) / 100
discount = 0
if number_nights > 7:
    discount = price_per_night * 0.05
price_per_night -= discount
total_price = number_nights * price_per_night
price_expenses = budget * percent_expenses

total = total_price + price_expenses

if budget >= total:
    money_left = budget - total
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
else:
    money_needed = total - budget
    print(f"{money_needed:.2f} leva needed.")
