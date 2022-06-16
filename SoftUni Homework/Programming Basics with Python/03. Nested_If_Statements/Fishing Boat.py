budget = int(input())
season = input()
number_fishermen = int(input())
discount_percent = 0
ship_rent = 0

if season == "Spring":
    ship_rent = 3000

elif season == "Summer" or season == "Autumn":
    ship_rent = 4200

elif season == "Winter":
    ship_rent = 2600

if number_fishermen <= 6:
    discount_percent = 0.1

elif 7 <= number_fishermen <= 11:
    discount_percent = 0.15

elif number_fishermen >= 12:
    discount_percent = 0.25

ship_rent -= ship_rent * discount_percent

if season != "Autumn" and number_fishermen % 2 == 0:
    discount_percent = 0.05
    ship_rent -= ship_rent * discount_percent

if budget >= ship_rent:
    money_left = budget - ship_rent
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = ship_rent - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")
