list_of_integers = list(map(int, input().split()))

is_even = lambda x: x % 2 == 0

filtered_numbers = list(filter(is_even, list_of_integers))

print(filtered_numbers)
