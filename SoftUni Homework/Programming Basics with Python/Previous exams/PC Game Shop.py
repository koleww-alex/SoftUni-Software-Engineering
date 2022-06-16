games_sold = int(input())

hearthstone = 0
fortnite = 0
overwatch = 0
others = 0

for _ in range(1, games_sold + 1):
    game_name = input()

    if game_name == "Hearthstone":
        hearthstone += 1
    elif game_name == "Fornite":
        fortnite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    else:
        others += 1

p_hearthstone = (hearthstone / games_sold) * 100
p_fortnite = (fortnite / games_sold) * 100
p_overwatch = (overwatch / games_sold) * 100
p_others = (others / games_sold) * 100

print(f"Hearthstone - {p_hearthstone:.2f}%\n"
      f"Fornite - {p_fortnite:.2f}%\n"
      f"Overwatch - {p_overwatch:.2f}%\n"
      f"Others - {p_others:.2f}%")
