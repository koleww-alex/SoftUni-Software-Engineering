items = input().split()
inventory = {items[i]: int(items[i + 1]) for i in range(0, len(items), 2)}

items_to_search = input().split()

for item in items_to_search:
    if item in inventory:
        print(f"We have {inventory.get(item)} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
