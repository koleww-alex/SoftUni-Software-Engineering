number_hrizantemi = int(input())
number_rozi = int(input())
number_laleta = int(input())
season = input()
holiday = input()

price_hrizantemi = 0
price_rozi = 0
price_laleta = 0
price_bucket = 0
total_price = 0

if season == "Spring":
    price_hrizantemi = number_hrizantemi * 2
    price_rozi = number_rozi * 4.10
    price_laleta = number_laleta * 2.50
    price_bucket = price_hrizantemi + price_rozi + price_laleta
    if number_laleta > 7:
        price_bucket -= price_bucket * 0.05
elif season == "Summer":
    price_hrizantemi = number_hrizantemi * 2
    price_rozi = number_rozi * 4.10
    price_laleta = number_laleta * 2.50
    price_bucket = price_hrizantemi + price_rozi + price_laleta
elif season == "Autumn":
    price_hrizantemi = number_hrizantemi * 3.75
    price_rozi = number_rozi * 4.50
    price_laleta = number_laleta * 4.15
    price_bucket = price_hrizantemi + price_rozi + price_laleta
elif season == "Winter":
    price_hrizantemi = number_hrizantemi * 3.75
    price_rozi = number_rozi * 4.50
    price_laleta = number_laleta * 4.15
    price_bucket = price_hrizantemi + price_rozi + price_laleta
    if number_rozi >= 10:
        price_bucket -= price_bucket * 0.10
if holiday == "Y":
    price_bucket += price_bucket * 0.15

if number_hrizantemi + number_rozi + number_laleta > 20:
    price_bucket -= price_bucket * 0.20
price_bucket += 2

print(f"{price_bucket:.2f}")
