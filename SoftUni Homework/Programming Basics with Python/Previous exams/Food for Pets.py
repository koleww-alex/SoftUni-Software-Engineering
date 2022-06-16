number_of_days = int(input())
total_amount_of_food = float(input())
cookies = 0
total_food_eaten_cat = 0
total_food_eaten_dog = 0
total_food_eaten = 0

for day in range(1, number_of_days + 1):
    daily_eaten_food_dog = int(input())
    daily_eaten_food_cat = int(input())

    total_food_for_the_day = daily_eaten_food_dog + daily_eaten_food_cat
    total_food_eaten += total_food_for_the_day

    total_food_eaten_cat += daily_eaten_food_cat
    total_food_eaten_dog += daily_eaten_food_dog

    if day % 3 == 0:
        cookies += total_food_for_the_day * 0.1

percent_total_food_eaten = (total_food_eaten / total_amount_of_food) * 100
percent_total_food_eaten_cat = (total_food_eaten_cat / total_food_eaten) * 100
percent_total_food_eaten_dog = (total_food_eaten_dog / total_food_eaten) * 100

print(f"Total eaten biscuits: {round(cookies)}gr.\n"
      f"{percent_total_food_eaten:.2f}% of the food has been eaten.\n"
      f"{percent_total_food_eaten_dog:.2f}% eaten from the dog.\n"
      f"{percent_total_food_eaten_cat:.2f}% eaten from the cat.\n")
