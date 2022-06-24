list_of_integers = list(map(int, input().split(", ")))
max_number = max(list_of_integers)

if max_number % 10 == 0:
    number_of_lists = int(max_number / 10)
else:
    number_of_lists = int(max_number / 10) + 1
cnt = 1

for list_of_numbers in range(1, number_of_lists + 1):
    group_of_numbers = []
    for number in list_of_integers:
        current_number = number
        if cnt <= current_number <= list_of_numbers * 10:
            group_of_numbers.append(current_number)
    cnt += 10
    print(f"Group of {list_of_numbers * 10}'s: {group_of_numbers}")

