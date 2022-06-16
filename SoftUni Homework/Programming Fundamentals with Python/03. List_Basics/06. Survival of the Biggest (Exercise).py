list_of_str = input().split()
n = int(input())
list_of_numbers = []

final_list = []

for element in list_of_str:
    list_of_numbers.append(int(element))

for _ in range(n):
    min_number = min(list_of_numbers)
    list_of_numbers.remove(min_number)

for number in list_of_numbers:
    final_list.append(str(number))

numbers = ", ".join(final_list)

print(numbers)
