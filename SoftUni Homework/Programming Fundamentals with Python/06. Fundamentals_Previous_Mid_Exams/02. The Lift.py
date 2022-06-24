waiting_passengers_cnt = int(input())
list_total_wagon_free_spaces = list(map(int, input().split()))

number_of_wagons = len(list_total_wagon_free_spaces)

for i in range(number_of_wagons):
    if waiting_passengers_cnt == 0:
        break
    if list_total_wagon_free_spaces[i] < 4:
        if list_total_wagon_free_spaces[i] != 0:
            left_spaces = 4 - list_total_wagon_free_spaces[i]
            if left_spaces > waiting_passengers_cnt:
                list_total_wagon_free_spaces[i] += waiting_passengers_cnt
                waiting_passengers_cnt = 0
            else:
                waiting_passengers_cnt -= left_spaces
                list_total_wagon_free_spaces[i] += left_spaces

        elif list_total_wagon_free_spaces[i] == 0:
            left_spaces = 4
            if left_spaces > waiting_passengers_cnt:
                list_total_wagon_free_spaces[i] += waiting_passengers_cnt
                waiting_passengers_cnt = 0
            else:
                waiting_passengers_cnt -= left_spaces
                list_total_wagon_free_spaces[i] += left_spaces

list_total_wagon_free_spaces_str = list((map(str, list_total_wagon_free_spaces)))

total_wagon_free_spaces = " ".join(list_total_wagon_free_spaces_str)

if waiting_passengers_cnt == 0 and sum(list_total_wagon_free_spaces) < number_of_wagons * 4:
    print("The lift has empty spots!\n"
          f"{total_wagon_free_spaces}")

elif waiting_passengers_cnt > 0:
    print(f"There isn't enough space! {waiting_passengers_cnt} people in a queue!\n"
          f"{total_wagon_free_spaces}")
else:
    print(total_wagon_free_spaces)
