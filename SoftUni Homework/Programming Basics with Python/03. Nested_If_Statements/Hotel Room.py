month = input()
total_nights = int(input())

studio_price = 0
apartment_price = 0
discount_percent = 0
total_apartment_price = 0
total_price_studio = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    total_apartment_price = total_nights * apartment_price
    total_price_studio = total_nights * studio_price
    if total_nights > 14:
        discount_percent = 0.3
        total_price_studio -= total_price_studio * discount_percent
    elif total_nights > 7:
        discount_percent = 0.05
        total_price_studio -= total_price_studio * discount_percent

elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    total_apartment_price = total_nights * apartment_price
    total_price_studio = total_nights * studio_price
    if total_nights > 14:
        discount_percent = 0.2
        total_price_studio -= total_price_studio * discount_percent

elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    total_apartment_price = total_nights * apartment_price
    total_price_studio = total_nights * studio_price
if total_nights > 14:
    discount_percent = 0.1
    total_apartment_price -= total_apartment_price * discount_percent

print(f"Apartment: {total_apartment_price:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
