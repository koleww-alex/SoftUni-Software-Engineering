trip_price = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

puzzle = 2.60
doll = 3
bear = 4.10
minion = 8.20
truck = 2

total_number = number_puzzles + number_dolls + number_bears + number_minions + number_trucks
total_price = (number_puzzles * puzzle) + (number_dolls * doll) + (number_bears * bear) + \
              (number_minions * minion) + (number_trucks * truck)

if total_number >= 50:
    discount = total_price * 0.25
    rent = (total_price - discount) * 0.1
    total_price -= discount
    final_price = total_price - rent
else:
    rent = total_price * 0.1
    final_price = total_price - rent

if final_price >= trip_price:
    print(f"Yes! {final_price - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - final_price:.2f} lv needed.")
