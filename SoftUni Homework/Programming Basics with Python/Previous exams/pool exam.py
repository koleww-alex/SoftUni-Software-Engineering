number_of_people = int(input())
entrance_tax = float(input())
price_per_bed = float(input())
price_per_umbrella = float(input())
from math import ceil
tax_price = number_of_people * entrance_tax
umbrellas_price = ceil((number_of_people / 2)) * price_per_umbrella
bed_price = ceil((number_of_people * 0.75)) * price_per_bed
finaL_sum = tax_price + umbrellas_price + bed_price
print(f"{finaL_sum:.2f} lv.")
