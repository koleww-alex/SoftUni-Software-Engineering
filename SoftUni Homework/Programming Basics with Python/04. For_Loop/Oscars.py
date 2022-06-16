actor_name = input()
academy_points = float(input())
number_judge = int(input())
name_judge = ""
total_points = 0

total_points += academy_points
for i in range(1, number_judge + 1):
    name_judge = input()
    points_judge = float(input())
    total_points += ((len(name_judge) * points_judge) / 2)

    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
if total_points < 1250.5:
    points_needed = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {points_needed:.1f} more!")



