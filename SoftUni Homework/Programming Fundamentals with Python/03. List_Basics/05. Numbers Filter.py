number_of_iterations = int(input())

list1 = []

filtered_list = []

for _ in range(1, number_of_iterations + 1):
    current_num = int(input())

    list1.append(current_num)

command = input()

if command == "even":
    for element in list1:

        if element % 2 == 0:
            filtered_list.append(element)

elif command == "odd":
    for element in list1:

        if element % 2 != 0:
            filtered_list.append(element)

elif command == "negative":
    for element in list1:

        if element < 0:
            filtered_list.append(element)

elif command == "positive":
    for element in list1:

        if element >= 0:
            filtered_list.append(element)

print(filtered_list)

