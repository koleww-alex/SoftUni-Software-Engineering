numbers = input()

list_numbers = numbers.split()
opposite_numbers = []
for element in list_numbers:
    opposite_numbers.append(-int(element))
print(opposite_numbers)
