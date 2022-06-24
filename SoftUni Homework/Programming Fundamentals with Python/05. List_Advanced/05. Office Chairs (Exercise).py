number_of_rooms = int(input())
free_chairs = 0
used_chairs = 0

for room in range(1, number_of_rooms + 1):
    list_of_information = input().split()
    chairs, visitors = list_of_information

    difference = abs(len(chairs) - int(visitors))

    if len(chairs) < int(visitors):
        print(f"{difference} more chairs needed in room {room}")
        used_chairs += difference
    else:
        free_chairs += difference

if free_chairs >= used_chairs:
    number_of_free_chairs = free_chairs - used_chairs
    print(f"Game On, {number_of_free_chairs} free chairs left")

