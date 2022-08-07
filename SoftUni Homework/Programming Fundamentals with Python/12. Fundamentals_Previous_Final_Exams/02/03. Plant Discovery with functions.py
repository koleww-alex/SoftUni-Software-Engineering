from collections import defaultdict


def rate(flower: str, current_rating: float):
    if flower in my_dict:
        my_dict_ratings[flower].append(current_rating)
        return my_dict_ratings
    return "error"


def update(flower: str, new_rare: int):
    if flower in my_dict:
        my_dict[flower] = new_rare
        return my_dict
    return "error"


def reset(flower: str):
    if flower in my_dict:
        my_dict_ratings[flower].clear()
        return my_dict_ratings
    return "error"


my_dict = defaultdict(int)
my_dict_ratings = defaultdict(list)
n = int(input())
for _ in range(n):
    info = input().split("<->")
    rarity = int(info[1])
    my_dict[info[0]] = rarity

while True:
    command = input()
    if command == "Exhibition":
        break
    current_command = command.split(": ")
    operation = current_command[0]

    if operation == "Rate":
        info = current_command[1].split(" - ")
        plant, rating = info[0], info[1]
        rating = float(rating)
        if rate(plant, rating) != "error":
            my_dict_ratings = rate(plant, rating)
        else:
            print(rate(plant, rating))

    elif operation == "Update":
        info = current_command[1].split(" - ")
        plant, new_rating = info[0], info[1]
        new_rating = int(new_rating)
        if update(plant, new_rating) != "error":
            my_dict = update(plant, new_rating)
        else:
            print(update(plant, new_rating))
    elif operation == "Reset":
        plant = current_command[1]
        if reset(plant) != "error":
            my_dict_ratings = reset(plant)
        else:
            print(reset(plant))

print("Plants for the exhibition:")

for key, value in my_dict.items():
    if not len(my_dict_ratings[key]) == 0:
        average_rating = sum(my_dict_ratings[key]) / len(my_dict_ratings[key])
    else:
        average_rating = 0
    print(f"- {key}; Rarity: {value}; Rating: {average_rating:.2f}")
