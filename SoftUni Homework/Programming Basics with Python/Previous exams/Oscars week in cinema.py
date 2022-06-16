movie_name = input()
hall_type = input()
number_tickets = int(input())
funds = 0
if movie_name == "A Star Is Born":
    if hall_type == "normal":
        funds += 7.50
    elif hall_type == "luxury":
        funds += 10.50
    else:
        funds += 13.50

elif movie_name == "Bohemian Rhapsody":
    if hall_type == "normal":
        funds += 7.35
    elif hall_type == "luxury":
        funds += 9.45
    else:
        funds += 12.75

elif movie_name == "Green Book":
    if hall_type == "normal":
        funds += 8.15
    elif hall_type == "luxury":
        funds += 10.25
    else:
        funds += 13.25

else:
    if hall_type == "normal":
        funds += 8.75
    elif hall_type == "luxury":
        funds += 11.55
    else:
        funds += 13.95

total_funds = funds * number_tickets

print(f"{movie_name} -> {total_funds:.2f} lv.")




