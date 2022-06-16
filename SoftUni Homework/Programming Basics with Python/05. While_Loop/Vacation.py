money_needed = float(input())
money_available = float(input())
days_cnt = 0
spend_days_cnt = 0

while money_available < money_needed and spend_days_cnt < 5:
    action = input()
    money_action = float(input())
    days_cnt += 1
    if action == "spend":
        money_available -= money_action
        spend_days_cnt += 1
        if money_available < 0:
            money_available = 0
    else:
        money_available += money_action
        spend_days_cnt = 0

if spend_days_cnt == 5:
    print("You can't save the money.")
    print(f"{days_cnt}")

if money_available >= money_needed:
    print(f"You saved the money for {days_cnt} days.")
