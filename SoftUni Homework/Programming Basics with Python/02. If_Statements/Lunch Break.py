movie = input()
episode_lenght = int(input())
break_lenght = int(input())
lunch_time = break_lenght * 0.125
chill_time = break_lenght * 0.25
break_lenght_left = break_lenght - lunch_time - chill_time
from math import ceil

if break_lenght_left >= episode_lenght:
    time_left = ceil(break_lenght_left - episode_lenght)
    print(f"You have enough time to watch {movie} and left with {time_left} minutes free time.")
else:
    time_needed = ceil(episode_lenght - break_lenght_left)
    print(f"You don't have enough time to watch {movie}, you need {time_needed} more minutes.")
