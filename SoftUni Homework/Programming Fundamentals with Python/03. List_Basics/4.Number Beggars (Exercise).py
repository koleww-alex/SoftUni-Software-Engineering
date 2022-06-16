list_of_strings = input().split(", ")
number_of_beggars = int(input())
list_of_numbers = []
index = 0

final_list = []

for element in list_of_strings:
    list_of_numbers.append(int(element))

while index < number_of_beggars:
    temp_sum = 0

    for current_index in range(index, len(list_of_numbers), number_of_beggars):

        temp_sum += list_of_numbers[current_index]

    final_list.append(temp_sum)
    index += 1

print(final_list)
