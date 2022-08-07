from collections import defaultdict

my_dict = defaultdict(int)
my_dict_ratings = defaultdict(list)

n = int(input())
for _ in range(n):
    info = input().split("<->")
    plant = info[0]
    rarity = int(info[1])
    my_dict[plant] = rarity

while True:
    command = input()
    if command == "Exhibition":
        break
    current_command = command.split(": ")
    operation = current_command[0]

    if operation == "Rate":
        info = current_command[1].split(" - ")
        plant, rating = info[0], int(info[1])
        if plant in my_dict:
            my_dict_ratings[plant].append(rating)
        else:
            print("error")

    elif operation == "Update":
        info = current_command[1].split(" - ")
        plant, new_rarity = info[0], int(info[1])
        if plant in my_dict:
            my_dict[plant] = new_rarity
        else:
            print("error")

    elif operation == "Reset":
        plant = current_command[1]
        if plant in my_dict:
            my_dict_ratings[plant].clear()
        else:
            print("error")

print("Plants for the exhibition:")

for key, value in my_dict.items():
    if len(my_dict_ratings[key]) == 0:
        average_rating = 0
    else:
        average_rating = sum(my_dict_ratings[key]) / len(my_dict_ratings[key])
    print(f"- {key}; Rarity: {value}; Rating: {average_rating:.2f}")
