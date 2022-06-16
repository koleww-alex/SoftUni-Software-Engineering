racing_field = list(map(int, input().split()))
half_field = len(racing_field) // 2

team_left_time = 0
team_right_time = 0

for number in range(half_field):
    if racing_field[number] != 0:
        team_left_time += racing_field[number]
    else:
        team_left_time -= team_left_time * 0.2
        if team_left_time < 0:
            team_left_time = 0
for number in range(half_field, len(racing_field)):
    if racing_field[number] != 0:
        team_right_time += racing_field[number]
    else:
        team_right_time -= team_right_time * 0.2
        if team_right_time < 0:
            team_right_time = 0


if team_left_time < team_right_time:
    print(f"The winner is left with total time: {team_left_time:.1f}")
else:
    print(f"The winner is right with total time: {team_right_time:.1f}")



