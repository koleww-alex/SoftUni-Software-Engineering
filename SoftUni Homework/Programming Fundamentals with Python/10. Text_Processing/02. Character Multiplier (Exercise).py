def string_one_is_longer(first_string: str, second_string: str):
    number = 0
    for i in range(len(second_string)):
        number += ord(first_string[i]) * ord(second_string[i])

    for i in range(len(second_string), len(first_string)):
        number += ord(first_string[i])
    return number


def string_two_is_longer(first_string: str, second_string: str):
    number = 0
    for i in range(len(first_string)):
        number += ord(first_string[i]) * ord(second_string[i])

    for i in range(len(first_string), len(second_string)):
        number += ord(second_string[i])
    return number


def equal_lenght(first_string: str, second_string: str):
    number = 0
    for i in range(len(first_string)):
        number += ord(first_string[i]) * ord(second_string[i])
    return number


string_one, string_two = input().split()

if len(string_one) > len(string_two):
    print(string_one_is_longer(string_one, string_two))

elif len(string_two) > len(string_one):
    print(string_two_is_longer(string_one, string_two))

elif len(string_one) == len(string_two):
    print(equal_lenght(string_one, string_two))
