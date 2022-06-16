n = int(input())
washer = float(input())
p = int(input())

money_per_birthday = 0
toys_count = 0
total_money = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        toys_count += 1
    else:
        money_per_birthday += (5 * i) - 1

total_money = money_per_birthday + (toys_count * p)

if total_money >= washer:
    money_left = total_money - washer
    print(f"Yes! {money_left:.2f}")
else:
    money_needed = washer - total_money
    print(f"No! {money_needed:.2f}")

