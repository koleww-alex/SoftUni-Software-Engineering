from math import ceil

number_people = int(input())
entrance_tax = float(input())
price_per_bed = float(input())
price_per_umbrella = float(input())

bed_users = number_people * 0.75

price_entrance_tax = number_people * entrance_tax

price_beds = ceil(number_people * 0.75) * price_per_bed

umbrella_users = number_people / 2
price_umbrellas = ceil(number_people / 2) * price_per_umbrella

total_sum = price_entrance_tax + price_beds + price_umbrellas

print(f"{total_sum:.2f} lv.")
