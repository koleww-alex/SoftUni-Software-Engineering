period = int(input())
electricity_bill = 0
water = 0
internet = 0
others = 0
for _ in range(1, period + 1):
    electricity = float(input())
    electricity_bill += electricity
    water += 20
    internet += 15
    others += ((electricity + 20 + 15) * 0.2) + electricity + 20 + 15

average = (electricity_bill + water + internet + others) / period

print(f"Electricity: {electricity_bill:.2f} lv\n"
f"Water: {water:.2f} lv\n"
f"Internet: {internet:.2f} lv\n"
f"Other: {others:.2f} lv\n"
f"Average: {average:.2f} lv")
