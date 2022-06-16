total_gifts = input().split()

command = input()

while command != "No Money":
    split = command.split()

    condition = split[0]
    type_of_product = split[1]

    if condition == "OutOfStock":
        for i in range(len(total_gifts)):
            if total_gifts[i] == type_of_product:
                total_gifts[i] = "None"

    elif condition == "Required":
        index = int(split[2])
        if index < len(total_gifts):
            total_gifts.pop(index)
            total_gifts.insert(index, type_of_product)

    elif condition == "JustInCase":
        total_gifts.insert(-1, type_of_product)
        total_gifts.pop()

    command = input()

iterations_number = total_gifts.count("None")

for _ in range(iterations_number):
    total_gifts.remove("None")

gifts = " ".join(total_gifts)
print(gifts)
