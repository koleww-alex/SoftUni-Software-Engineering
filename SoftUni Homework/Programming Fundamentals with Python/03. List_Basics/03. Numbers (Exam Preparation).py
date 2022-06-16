list_of_strings = input().split()

lenght_of_list = len(list_of_strings)

list_of_numbers = []

top_five_biggest_numbers = []

for element in list_of_strings:
    list_of_numbers.append(int(element))

list_sum = sum(list_of_numbers)

average_value_in_list = list_sum / lenght_of_list

for i in range(5):
    list_of_numbers.sort(reverse=True)

    if list_of_numbers[i] > average_value_in_list:
        top_five_biggest_numbers.append(list_of_numbers[i])
    else:
        break
top_five_biggest_strings = []

top_five_biggest_numbers.sort(reverse=True)

for number in top_five_biggest_numbers:
    top_five_biggest_strings.append(str(number))

if len(top_five_biggest_numbers) == 0:
    print("No")
else:
    separated_strings = " ".join(top_five_biggest_strings)
    print(separated_strings)

