food_in_grams = float(input()) * 1000
hay_in_grams = float(input()) * 1000
cover_in_grams = float(input()) * 1000
pig_weight_in_kilos = float(input()) * 1000

merry_must_go_to_store = False

for day in range(1, 30 + 1):

    food_in_grams -= 300

    if day % 2 == 0:
        hay_in_grams -= food_in_grams * 0.05

    if day % 3 == 0:
        cover_in_grams -= pig_weight_in_kilos / 3

    if food_in_grams <= 0 or hay_in_grams <= 0 or cover_in_grams <= 0:
        merry_must_go_to_store = True
        break


if not merry_must_go_to_store:
    print(f"Everything is fine! Puppy is happy! Food: {food_in_grams / 1000:.2f}, Hay: {hay_in_grams / 1000:.2f},"
          f" Cover: {cover_in_grams / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")
