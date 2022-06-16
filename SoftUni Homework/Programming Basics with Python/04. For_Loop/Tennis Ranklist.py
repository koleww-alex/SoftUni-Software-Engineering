from math import floor

number_tournaments = int(input())
starting_points = int(input())
points = 0
winner = 0
for _ in range(1, number_tournaments + 1):
    position = input()

    if position == "W":
        points += 2000
        winner += 1
    elif position == "F":
        points += 1200
    else:
        points += 720

percent_winner = (winner / number_tournaments) * 100

average_points = (points / number_tournaments)

points += starting_points

print(f"Final points: {points}\n"
      f"Average points: {floor(average_points)}\n"
      f"{percent_winner:.2f}%")
