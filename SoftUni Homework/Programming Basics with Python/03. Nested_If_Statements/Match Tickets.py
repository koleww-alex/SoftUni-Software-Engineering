budget = float(input())
ticket_type = input()
group_number = int(input())

vip_ticket = 499.99
normal_ticket = 249.99

tickets_price = 0
transport_price = 0

if ticket_type == "Normal":
    tickets_price = group_number * normal_ticket
else:
    tickets_price = group_number * vip_ticket

if 1 <= group_number <= 4:
    transport_price = budget * 0.75

elif 5 <= group_number <= 9:
    transport_price = budget * 0.6

elif 10 <= group_number <= 24:
    transport_price = budget * 0.5

elif 25 <= group_number <= 49:
    transport_price = budget * 0.4

else:
    transport_price = budget * 0.25

total_price = tickets_price + transport_price

if budget >= total_price:
    money_left = budget - total_price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = total_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")
