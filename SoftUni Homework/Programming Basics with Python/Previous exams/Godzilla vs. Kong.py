film_budget = float(input())
number_statist = int(input())
dress_price_per_statist = float(input())

decor = film_budget * 0.1

if number_statist >= 150:
    dress_price_per_statist -= dress_price_per_statist * 0.1

dress_cost = number_statist * dress_price_per_statist

total = decor + dress_cost

if film_budget >= total:
    money_left = film_budget - total
    print(f"Action!\n"
          f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    money_needed = total - film_budget
    print(f"Not enough money!\n"
          f"Wingard needs {money_needed:.2f} leva more.")

