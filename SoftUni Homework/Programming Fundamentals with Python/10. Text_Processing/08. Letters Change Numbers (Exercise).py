list_of_strings = input().strip().split()
total_sum = 0
for element in list_of_strings:
    first_letter = element[0]
    last_letter = element[-1]
    number = int(element[1:len(element) - 1])
    first_letter_position = ord(first_letter.lower()) - 96
    last_letter_position = ord(last_letter.lower()) - 96

    if first_letter == first_letter.upper():
        number = number / first_letter_position
    elif first_letter == first_letter.lower():
        number = number * first_letter_position

    if last_letter == last_letter.upper():
        number = number - last_letter_position
    elif last_letter == last_letter.lower():
        number = number + last_letter_position

    total_sum += number

print(f"{total_sum:.2f}")
