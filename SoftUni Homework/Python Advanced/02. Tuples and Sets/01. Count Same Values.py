numbers = tuple(map(float, input().split()))
# USING LISTS

numbers_count = []
for number in numbers:
    if f'{number} - {numbers.count(number)} times' not in numbers_count:
        numbers_count.append(f'{number} - {numbers.count(number)} times')

print('\n'.join(numbers_count))

# USING DICTIONARIES

numbers_count = {}
for number in numbers:
    if number not in numbers_count:
        numbers_count[number] = numbers.count(number)

for key, value in numbers_count.items():
    print(f'{key} - {value} times')

