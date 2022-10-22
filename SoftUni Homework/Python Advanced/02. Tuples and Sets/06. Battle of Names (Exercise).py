N = int(input())
even_numbers = set()
odd_numbers = set()

for i in range(1, N + 1):
    current_name = input()
    temp_sum = 0
    for ch in current_name:
        temp_sum += ord(ch)

    temp_sum //= i
    if temp_sum % 2 == 0:
        even_numbers.add(temp_sum)
    else:
        odd_numbers.add(temp_sum)

if sum(even_numbers) == sum(odd_numbers):
    union_values = odd_numbers.union(even_numbers)
    str_numbers = [str(x) for x in union_values]
    print(', '.join(str_numbers))

elif sum(odd_numbers) > sum(even_numbers):
    different_value = odd_numbers.difference(even_numbers)
    str_numbers = [str(x) for x in different_value]
    print(', '.join(str_numbers))

elif sum(even_numbers) > sum(odd_numbers):
    symmetric_diff_values = odd_numbers.symmetric_difference(even_numbers)
    str_numbers = [str(x) for x in symmetric_diff_values]
    print(', '.join(str_numbers))
