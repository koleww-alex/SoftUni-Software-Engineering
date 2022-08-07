import re
pattern = r"%([A-Z][a-z]+)%<(\w+)>\w*\|(\d+)\|(\w*\d+\.?\d+)\$"
total_income = 0
while True:
    command = input()
    if command == "end of shift":
        break
    matches = re.findall(pattern, command)
    for match in matches:
        customer, product, quantity, price = match
        quantity = int(quantity)
        new_price = ""
        for ch in price:
            if ch.isdigit() or ch == ".":
                new_price += ch
        new_price = float(new_price)
        current_income = quantity * new_price
        total_income += current_income
        print(f"{customer}: {product} - {current_income:.2f}")

print(f"Total income: {total_income:.2f}")
