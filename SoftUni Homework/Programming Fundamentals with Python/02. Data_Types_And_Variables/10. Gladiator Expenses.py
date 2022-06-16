lost_fights_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_cost = 0
shield_brake_cnt = 0

for lost_game in range(1, lost_fights_count + 1):

    if lost_game % 2 == 0:
        total_cost += helmet_price

    if lost_game % 3 == 0:
        total_cost += sword_price

    if lost_game % 2 == 0 and lost_game % 3 == 0:
        total_cost += shield_price
        shield_brake_cnt += 1

    if shield_brake_cnt == 2:
        total_cost += armor_price
        shield_brake_cnt = 0

print(f"Gladiator expenses: {total_cost:.2f} aureus")
