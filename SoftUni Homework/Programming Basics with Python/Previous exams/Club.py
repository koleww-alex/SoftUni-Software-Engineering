wanted_profit = float(input())
command = input()
income = 0
profit_acquired = False

while command != "Party!":
    price_cocktail = len(command)
    number_cocktails = int(input())
    price = price_cocktail * number_cocktails
    income += price

    if price % 2 != 0:
        income -= price * 0.25

    if income >= wanted_profit:
        profit_acquired = True
        break

    command = input()

if profit_acquired:
    print("Target acquired.")
    print(f"Club income - {income:.2f} leva.")
else:
    money_needed = wanted_profit - income
    print(f"We need {money_needed:.2f} leva more.")
    print(f"Club income - {income:.2f} leva.")