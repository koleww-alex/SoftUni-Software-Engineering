number_of_days_of_tournament = int(input())
total_games_won = 0
total_games_lost = 0

total_money_saved = 0
for _ in range(1, number_of_days_of_tournament + 1):
    sport = input()
    money_saved_for_the_day = 0
    games_won = 0
    games_lost = 0

    while sport != "Finish":
        result = input()

        if result == "win":
            money_saved_for_the_day += 20
            games_won += 1
        else:
            games_lost += 1

        total_games_won += games_won
        total_games_lost += games_lost

        sport = input()

    if games_won > games_lost:
        money_saved_for_the_day += money_saved_for_the_day * 0.1
    total_money_saved += money_saved_for_the_day

if total_games_won > total_games_lost:
    total_money_saved += total_money_saved * 0.2
    print(f"You won the tournament! Total raised money: {total_money_saved:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money_saved:.2f}")
