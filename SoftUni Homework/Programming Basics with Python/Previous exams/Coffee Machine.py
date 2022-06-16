drink = input()
sugar = input()
number_drinks = int(input())

if drink == "Espresso":
    if sugar == "Without":
        drink_price = 0.90
    elif sugar == "Normal":
        drink_price = 1
    else:
        drink_price = 1.20
elif drink == "Cappuccino":
    if sugar == "Without":
        drink_price = 1
    elif sugar == "Normal":
        drink_price = 1.20
    else:
        drink_price = 1.60
else:
    if sugar == "Without":
        drink_price = 0.50
    elif sugar == "Normal":
        drink_price = 0.60
    else:
        drink_price = 0.70

price = drink_price * number_drinks

if sugar == "Without":
    price -= price * 0.35

if drink == "Espresso":
    if number_drinks >= 5:
        price -= price * 0.25

if price > 15:
    price -= price * 0.2

print(f"You bought {number_drinks} cups of {drink} for {price:.2f} lv.")
