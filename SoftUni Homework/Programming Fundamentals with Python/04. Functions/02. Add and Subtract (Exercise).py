def sum_numbers(first_num, second_num):
    sum_of_numbers = first_num + second_num
    return sum_of_numbers


def subtract(sum_of_numbers, third_num):
    result = sum_of_numbers - third_num
    return result


def add_and_subtract(first_num, second_num, third_num):
    sum_of_first_and_second_num = sum_numbers(first_num, second_num)
    result = subtract(sum_of_first_and_second_num, third_num)
    return result


number_one = int(input())
number_two = int(input())
number_three = int(input())


print(add_and_subtract(number_one, number_two, number_three))
