list_of_integers = list(map(int, input().split()))
command = input()

while command != "end":
    current_command = list(command.split())

    operation = current_command[0]

    if operation == "swap":
        first_element = int(current_command[1])
        second_element = int(current_command[2])

        list_of_integers[first_element], list_of_integers[second_element] = \
            list_of_integers[second_element], list_of_integers[first_element]

    elif operation == "multiply":
        first_element = int(current_command[1])
        second_element = int(current_command[2])

        first_number = list_of_integers[first_element]
        second_number = list_of_integers[second_element]
        result = first_number * second_number

        list_of_integers.pop(first_element)
        list_of_integers.insert(first_element, result)

    elif operation == "decrease":
        for index in range(len(list_of_integers)):
            current_number = list_of_integers[index]
            current_number -= 1
            list_of_integers.pop(index)
            list_of_integers.insert(index, current_number)

    command = input()

list_of_strings = []

for number in list_of_integers:
    list_of_strings.append(str(number))


strings_out_of_list = ", ".join(list_of_strings)
print(strings_out_of_list)
