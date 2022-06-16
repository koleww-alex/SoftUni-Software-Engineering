from math import floor

number_of_centuries = int(input())

years_in_centuries = number_of_centuries * 100

days = floor(years_in_centuries * 365.2422)

hours = floor(days * 24)

minutes = floor(hours * 60)

print(f"{number_of_centuries} centuries = {years_in_centuries} years = {days} days = {hours} hours = {minutes} minutes")

