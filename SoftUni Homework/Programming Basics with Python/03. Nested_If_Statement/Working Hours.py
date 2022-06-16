hour = int(input())
day = input()

if 10 <= hour <= 18 and day != "Sunday":
    print("open")
else:
    print("closed")

# Не използвай or + and, защото правят грешки!!!!

# if 10 <= hour <= 18 and day == "Monday" or day == "Tuesday" or day == "Wednesday"\
#         or day == "Thursday" or day == "Friday" or day == "Saturday":
#     print("open")
# else:
#     print("closed")

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
    if 10 <= hour <= 18:
        print("open")
else:
    print("closed")
