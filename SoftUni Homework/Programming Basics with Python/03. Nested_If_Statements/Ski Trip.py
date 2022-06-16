trip_days = int(input())
room_type = input()
grade = input()

total_price = 0
room_for_one_person = 18.00
apartment = 25.00
president_apartment = 35.00
total_night = trip_days - 1

if room_type == "room for one person":
    total_price = total_night * 18.00
elif room_type == "apartment":
    total_price = total_night * 25.00
    if total_night < 10:
        total_price -= total_price * 0.3
    elif 10 <= total_night < 15:
        total_price -= total_price * 0.35
    else:
        total_price -= total_price * 0.5
elif room_type == "president apartment":
    total_price = total_night * 35.00
    if total_night < 10:
        total_price -= total_price * 0.1
    elif 10 <= total_night < 15:
        total_price -= total_price * 0.15
    else:
        total_price -= total_price * 0.20

if grade == "positive":
    total_price += total_price * 0.25
else:
    total_price -= total_price * 0.1

print(f"{total_price:.2f}")
