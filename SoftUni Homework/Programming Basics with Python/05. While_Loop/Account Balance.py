money = ""
total_money = 0

while money != "NoMoreMoney":
    money = input()
    if money == "NoMoreMoney":
        break
    money = float(money)
    if money >= 0:
        print(f"Increase: {money:.2f}")
        total_money += money
    else:
        print("Invalid operation!")
        break
print(f"Total: {total_money:.2f}")
