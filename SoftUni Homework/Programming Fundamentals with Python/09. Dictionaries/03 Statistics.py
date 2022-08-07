command = input()
inventory = {}
while command != "statistics":
    current_command = command.split(": ")
    product = current_command[0]
    quantity = int(current_command[1])
    if product not in inventory:
        inventory[product] = quantity
    else:
        inventory[product] += quantity

    command = input()

print("Products in stock:")

product_presentation = [f'- {item}: {str(inventory[item])}' for item in inventory]
print("\n".join(product_presentation))
print(f"Total Products: {len(inventory.values())}")
print(f"Total Quantity: {sum(inventory.values())}")
