list_of_numbers = list(map(int, input().split(", ")))

even_number_indices = [num for num in range(len(list_of_numbers))
                       if list_of_numbers[num] % 2 == 0]
print(even_number_indices)
