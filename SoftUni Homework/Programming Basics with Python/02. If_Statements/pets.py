number_days = int(input())
food_left = int(input())
dog_food_day = float(input())
cat_food_day = float(input())
turtle_food_day = float(input()) / 1000

from math import floor, ceil

dog_food = dog_food_day * number_days
cat_food = cat_food_day * number_days
turtle_food = turtle_food_day * number_days
sum_food = dog_food + cat_food + turtle_food

if sum_food <= food_left:
    print(f'{floor(food_left - sum_food)} kilos of food left.')
else:
    print(f'{ceil(sum_food - food_left)} more kilos of food are needed.')
