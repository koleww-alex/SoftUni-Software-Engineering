list_of_info = input().split("#")
water = int(input())
total_effort = 0
total_fire = 0

print("Cells:")

for element in list_of_info:
    divided_list = element.split(" =")

    type_of_fire = divided_list[0]
    cell_value = int(divided_list[1])

    if type_of_fire == "High" and 81 <= cell_value <= 125 and water >= cell_value:
        water -= cell_value
        total_fire += cell_value
        total_effort += cell_value * 0.25
        print(f" - {cell_value}")
    elif type_of_fire == "Medium" and 51 <= cell_value <= 80 and water >= cell_value:
        water -= cell_value
        total_fire += cell_value
        total_effort += cell_value * 0.25
        print(f" - {cell_value}")
    elif type_of_fire == "Low" and 1 <= cell_value <= 50 and water >= cell_value:
        water -= cell_value
        total_fire += cell_value
        total_effort += cell_value * 0.25
        print(f" - {cell_value}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
