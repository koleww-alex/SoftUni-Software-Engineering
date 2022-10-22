list_of_numbers = input().split()
list_of_reversed_numbers = [list_of_numbers[x] for x in range(len(list_of_numbers) - 1, -1, -1)]
print(' '.join(list_of_reversed_numbers))
