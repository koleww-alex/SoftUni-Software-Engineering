def stock_availability(inventory: list, command: str, *args):
    if command == 'delivery':
        for item in args:
            inventory.append(item)
    elif command == 'sell':
        if args:
            for item in args:
                if str(item).isdigit():
                    for _ in range(item):
                        inventory.pop(0)

                elif item in inventory:
                    times_to_remove = inventory.count(item)
                    for _ in range(times_to_remove):
                        inventory.remove(item)
        else:
            inventory.pop(0)

    return inventory


