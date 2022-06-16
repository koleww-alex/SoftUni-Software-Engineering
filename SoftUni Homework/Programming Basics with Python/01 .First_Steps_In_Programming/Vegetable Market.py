price_per_kilo_veg = float(input())
price_per_kilo_fruit = float(input())
total_kilos_veg = int(input())
total_kilos_fruit = int(input())
sum_leva = (price_per_kilo_veg * total_kilos_veg) + (price_per_kilo_fruit * total_kilos_fruit)
sum_euro = sum_leva / 1.94
print(f"{sum_euro:.2f}")