days_off = int(input())
work_day = 63
break_days = 127
work_days = 365 - days_off
play_time = days_off * 127 + work_days * 63

if play_time < 30000:
    sleep_time_hours = (30000 - play_time) // 60
    sleep_time_min = (30000 - play_time) % 60
    print(f"Tom sleeps well")
    print(f"{sleep_time_hours} hours and {sleep_time_min} minutes less for play")
else:
    sleep_time_hours = (play_time - 30000) // 60
    sleep_time_min = (play_time - 30000) % 60
    print(f"Tom will run away")
    print(f"{sleep_time_hours} hours and {sleep_time_min} minutes more for play")

