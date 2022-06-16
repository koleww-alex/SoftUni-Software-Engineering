command = input()
total_steps = 0
goal_reached = False
while command != "Going home":
    steps = int(command)
    total_steps += steps
    if total_steps >= 10000:
        goal_reached = True
        break
    command = input()

if command == "Going home":
    steps_home = int(input())
    total_steps += steps_home
if total_steps >= 10000:
    steps_diff = abs(total_steps - 10000)
    print("Goal reached! Good job!")
    print(f"{steps_diff} steps over the goal!")
else:
    steps_diff = abs(total_steps - 10000)
    print(f"{steps_diff} more steps to reach goal.")
