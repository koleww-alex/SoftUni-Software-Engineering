def positive(list_of_integers):
    list_of_positives = []
    for number in list_of_integers:
        if int(number) >= 0:
            list_of_positives.append(str(number))
    return f"Positive: {', '.join(list_of_positives)}"


def negative(list_of_integers):
    list_of_negatives = []
    for number in list_of_integers:
        if int(number) < 0:
            list_of_negatives.append(str(number))
    return f"Negative: {', '.join(list_of_negatives)}"


def even(list_of_integers):
    list_of_even = []
    for number in list_of_integers:
        if int(number) % 2 == 0:
            list_of_even.append(str(number))
    return f"Even: {', '.join(list_of_even)}"


def odd(list_of_integers):
    list_of_odd = []
    for number in list_of_integers:
        if int(number) % 2 != 0:
            list_of_odd.append(str(number))
    return f"Odd: {', '.join(list_of_odd)}"


list_of_numbers = list(map(int, input().split(", ")))

print(positive(list_of_numbers))
print(negative(list_of_numbers))
print(even(list_of_numbers))
print(odd(list_of_numbers))
