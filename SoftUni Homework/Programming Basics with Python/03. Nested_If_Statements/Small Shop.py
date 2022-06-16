product = input()
city = input()
quantity = float(input())
final_price = 0
if city == "Sofia":
    if product == "coffee":
        final_price = quantity * 0.50
    elif product == "water":
        final_price = quantity * 0.80
    elif product == "beer":
        final_price = quantity * 1.20
    elif product == "sweets":
        final_price = quantity * 1.45
    elif product == "peanuts":
        final_price = quantity * 1.60

elif city == "Plovdiv":
    if product == "coffee":
        final_price = quantity * 0.40
    elif product == "water":
        final_price = quantity * 0.70
    elif product == "beer":
        final_price = quantity * 1.15
    elif product == "sweets":
        final_price = quantity * 1.30
    elif product == "peanuts":
        final_price = quantity * 1.50

elif city == "Varna":
    if product == "coffee":
        final_price = quantity * 0.45
    elif product == "water":
        final_price = quantity * 0.70
    elif product == "beer":
        final_price = quantity * 1.10
    elif product == "sweets":
        final_price = quantity * 1.35
    elif product == "peanuts":
        final_price = quantity * 1.55

print(final_price)
