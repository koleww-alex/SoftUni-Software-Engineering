apartment_width = int(input())
apartment_lenght = int(input())
apartment_height = int(input())
command = input()
box_cnt = 0
box_size = 1
apartment_size = apartment_width * apartment_lenght * apartment_height

while command != "Done":
    box_cnt += int(command)

    if box_cnt > apartment_size:
        needed_meters = box_cnt - apartment_size
        print(f"No more free space! You need {needed_meters} Cubic meters more.")
        break
    command = input()

if command == "Done":
    meters_left = apartment_size - box_cnt
    print(f"{meters_left} Cubic meters left.")
