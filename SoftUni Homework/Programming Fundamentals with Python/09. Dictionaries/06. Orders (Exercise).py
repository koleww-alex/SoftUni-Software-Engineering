command = input().split()
my_dict = {}
while "buy" not in command:
    key, price, quantity = command
    price, quantity = float(price), int(quantity)
    if key not in my_dict:
        my_dict[key] = []
        my_dict[key].append(price)
        my_dict[key].append(quantity)
    else:
        my_dict[key][0] = price
        my_dict[key][1] += quantity

    command = input().split()

for key, value in my_dict.items():

    print(f"{key} -> {(my_dict[key][0] * my_dict[key][1]):.2f}")
