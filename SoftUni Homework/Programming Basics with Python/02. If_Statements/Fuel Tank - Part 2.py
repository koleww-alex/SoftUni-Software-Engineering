fuel_type = input()
liters_fuel = float(input())
club_card = input()

gasoline_price_liter = 2.22
diesel_price_liter = 2.33
gas_price_liter = 0.93

if fuel_type == "Diesel":
    raw_price = liters_fuel * diesel_price_liter
elif fuel_type == "Gasoline":
    raw_price = liters_fuel * gasoline_price_liter
else:
    raw_price = liters_fuel * gas_price_liter

if club_card == "Yes":
    if fuel_type == "Diesel":
        club_discount = diesel_price_liter - 0.12
        raw_price = liters_fuel * club_discount
    elif fuel_type == "Gasoline":
        club_discount = gasoline_price_liter - 0.18
        raw_price = liters_fuel * club_discount
    else:
        club_discount = gas_price_liter - 0.08
        raw_price = liters_fuel * club_discount

if 20 <= liters_fuel <= 25:
    discount = raw_price * 0.08
    raw_price = raw_price - discount
elif liters_fuel > 25:
    discount = raw_price * 0.1
    raw_price = raw_price - discount

print(f"{raw_price:.2f} lv.")

