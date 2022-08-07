dict_of_items = {"shards": 0, "fragments": 0, "motes": 0}
reached = False
while True:
    items = input().split()
    for i in range(0, len(items), 2):
        value = int(items[i])
        key = items[i + 1]
        key = key.lower()

        if key not in dict_of_items:
            dict_of_items[key] = 0

        dict_of_items[key] += value
        if dict_of_items["shards"] >= 250:
            dict_of_items["shards"] -= 250
            print("Shadowmourne obtained!")
            reached = True

        elif dict_of_items["fragments"] >= 250:
            dict_of_items["fragments"] -= 250
            print("Valanyr obtained!")
            reached = True

        elif dict_of_items["motes"] >= 250:
            dict_of_items["motes"] -= 250
            print("Dragonwrath obtained!")
            reached = True

        if reached:
            break
    if reached:
        break

print("\n".join(f"{key}: {value}" for key, value in dict_of_items.items()))
