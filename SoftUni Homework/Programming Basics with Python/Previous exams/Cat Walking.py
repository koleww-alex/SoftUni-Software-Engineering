minutes_walking = int(input())
number_of_walks = int(input())
calories_taken = int(input())

calories_burnt = minutes_walking * 5 * number_of_walks

needed_burnt_calories = calories_taken / 2

if calories_burnt >= needed_burnt_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burnt}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burnt}.")
