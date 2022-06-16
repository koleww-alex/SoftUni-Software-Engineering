name = input()

is_hetrick = False

best_player = ""
best_player_goals = 0

while name != "END":
    number_of_goals = int(input())

    if number_of_goals > best_player_goals:
        best_player_goals = number_of_goals
        best_player = name

    if best_player_goals >= 3:
        is_hetrick = True

    if best_player_goals >= 10:
        break

    name = input()

print(f"{best_player} is the best player!")

if is_hetrick:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")
