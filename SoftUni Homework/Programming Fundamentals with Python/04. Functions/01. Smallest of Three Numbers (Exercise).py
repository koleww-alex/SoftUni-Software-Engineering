def min_number(first_num, second_num, third_num):
    list_of_numbers = [first_num, second_num, third_num]

    smallest_number = min(list_of_numbers)
    return smallest_number


number_one = int(input())
number_two = int(input())
number_three = int(input())


print(min_number(number_one, number_two, number_three))
