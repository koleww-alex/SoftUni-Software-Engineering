total_amount_of_food = int(input()) * 1000
command = input()
total_amount_eaten = 0

while command != "Adopted":
    food_eaten = int(command)
    total_amount_eaten += food_eaten

    command = input()

diff = abs(total_amount_of_food - total_amount_eaten)

if total_amount_of_food >= total_amount_eaten:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
