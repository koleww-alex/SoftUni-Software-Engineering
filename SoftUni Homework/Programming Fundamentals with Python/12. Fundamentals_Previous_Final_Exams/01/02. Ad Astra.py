import re

pattern = r"#([A-Za-z\s]+)#(\d{2}\/\d{2}\/\d{2})#(\d+)#|\|([A-Za-z]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|"
info = input()
matches = re.findall(pattern, info)
total_cal = 0
all_items = []
for match in matches:
    list_of_info = []
    for element in match:
        if element != "":
            list_of_info.append(element)
            all_items.append(element)
    total_cal += int(list_of_info[2])

print(f"You have food to last you for: {total_cal // 2000} days!")

print("\n".join(f"Item: {all_items[i]}, Best before: {all_items[i + 1]}, Nutrition: {all_items[i + 2]}"
                for i in range(0, len(all_items), 3)))
