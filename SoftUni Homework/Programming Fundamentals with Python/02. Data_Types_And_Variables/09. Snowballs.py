from sys import maxsize

number_of_snowballs = int(input())
best_snowball = -maxsize

best_snowball_weight = 0
best_flying_time = 0
best_snowball_value = 0
best_snowball_quality = 0

for _ in range(1, number_of_snowballs + 1):
    snowball_weight = int(input())
    flying_time = int(input())
    snowball_quality = int(input())

    snowball_value = int((snowball_weight / flying_time) ** snowball_quality)

    if snowball_value > best_snowball:
        best_snowball = snowball_value
        best_snowball_weight = snowball_weight
        best_flying_time = flying_time
        best_snowball_value = snowball_value
        best_snowball_quality = snowball_quality

print(f"{best_snowball_weight} : {best_flying_time} = {best_snowball_value} ({best_snowball_quality})")

