number_of_people = int(input())
season = input()

discount = 0
higher_tax_rate = 0

if season == "spring":
    if number_of_people <= 5:
        price = number_of_people * 50
    else:
        price = number_of_people * 48


elif season == "summer":
    if number_of_people <= 5:
        price = number_of_people * 48.50
    else:
        price = number_of_people * 45

    discount = price * 0.15

elif season == "autumn":
    if number_of_people <= 5:
        price = number_of_people * 60
    else:
        price = number_of_people * 49.50

else:
    if number_of_people <= 5:
        price = number_of_people * 86
    else:
        price = number_of_people * 85
    higher_tax_rate = price * 0.08


price -= discount
price += higher_tax_rate


print(f"{price:.2f} leva.")

