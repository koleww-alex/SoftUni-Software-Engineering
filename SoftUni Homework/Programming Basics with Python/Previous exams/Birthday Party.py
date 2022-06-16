hall_rent = float(input())

cake = hall_rent * 0.2

drinks = cake - (cake * 0.45)

animator = hall_rent / 3

needed_budget = hall_rent + cake + drinks + animator

print(needed_budget)
