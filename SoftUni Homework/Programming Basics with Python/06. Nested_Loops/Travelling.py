destination = input()

while destination != "End":
    money_saved = 0
    money_needed = float(input())
    money = input()
    while money != "End":
        money = float(money)
        money_saved += money

        if money_saved >= money_needed:
            print(f"Going to {destination}!")
            break

        money = input()

    destination = input()
