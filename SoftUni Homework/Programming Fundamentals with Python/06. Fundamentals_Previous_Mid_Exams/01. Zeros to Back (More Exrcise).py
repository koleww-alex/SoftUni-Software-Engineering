list_of_integers = list(map(int, input().split(", ")))

list_of_zeroes = []
list_of_else = []

for number in list_of_integers:
    if number == 0:
        list_of_zeroes.append(0)
    else:
        list_of_else.append(number)

for number in list_of_zeroes:
    list_of_else.append(number)

print(list_of_else)

