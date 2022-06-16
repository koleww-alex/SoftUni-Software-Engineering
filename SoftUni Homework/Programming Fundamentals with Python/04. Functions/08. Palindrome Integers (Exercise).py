def palindrome(list_of_numbers):
    for number in list_of_numbers:
        number = str(number)
        if number == number[::-1]:
            print("True")
        else:
            print("False")
    return ""

list_of_integers = list(map(int, input().split(", ")))

print(palindrome(list_of_integers))

