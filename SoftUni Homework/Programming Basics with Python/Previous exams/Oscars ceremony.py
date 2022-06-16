hall_rent = int(input())

statues = hall_rent - (hall_rent * 0.3)
catering = statues - (statues * 0.15)
music = catering / 2

total = statues + catering + music + hall_rent

print(f"{total:.2f}")
