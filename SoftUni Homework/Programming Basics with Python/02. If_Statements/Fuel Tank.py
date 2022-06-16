fuel_type = input()
liters_left = int(input())

if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
    if liters_left >= 25:
        print(f"You have enough {str.lower(fuel_type)}.")
    else:
        print(f"Fill your tank with {str.lower(fuel_type)}!")
else:
    print("Invalid fuel!")

