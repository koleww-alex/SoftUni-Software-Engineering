import re
pattern = r">>([A-Za-z]+)<<(\d+\.?\d+)!(\d+)"
total_price = 0
furniture_bought = []
while True:
    command = input()
    if command == "Purchase":
        break
    match = re.findall(pattern, command)
    if match:
        furniture, price, quantity = match[0]
        total_price += float(price) * int(quantity)
        furniture_bought.append(furniture)

print("Bought furniture:")
for furniture in furniture_bought:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")
