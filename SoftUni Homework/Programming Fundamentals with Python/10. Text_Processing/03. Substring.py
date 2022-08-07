def string_cleaner(first_string: str, second_string: str):
    second_string = second_string.replace(first_string, "")
    return second_string


first = input()
second = input()

while first in second:
    second = string_cleaner(first, second)
print(second)
