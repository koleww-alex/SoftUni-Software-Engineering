film_budget = float(input())
number_of_statist = int(input())
price_per_dress_statist = float(input())
decor = film_budget * 0.1

if number_of_statist > 150:
    discount = (price_per_dress_statist * number_of_statist) * 0.1
    expenses = (number_of_statist * price_per_dress_statist - discount) + decor
else:
    expenses = (number_of_statist * price_per_dress_statist) + decor

if expenses > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {expenses - film_budget:.2f} leva more.")
else:
    print(f"Action!" )
    print(f"Wingard starts filming with {film_budget - expenses:.2f} leva left.")
