list_numbers = list(map(int, input().split()))
removed_numbers = []

while len(list_numbers) > 0:
    current_index = int(input())

    if current_index < 0:
        removed_numbers.append(list_numbers[0])
        list_numbers.pop(0)
        list_numbers.insert(0, list_numbers[-1])

    elif current_index >= len(list_numbers):
        removed_numbers.append(list_numbers[-1])
        list_numbers.pop()
        list_numbers.insert(list_numbers[-1], list_numbers[0])
    else:
        removed_numbers.append(list_numbers[current_index])
        list_numbers.pop(current_index)

    for i in range(len(list_numbers)):
        if list_numbers[i] <= removed_numbers[-1]:

            list_numbers[i] += removed_numbers[-1]
        else:
            list_numbers[i] -= removed_numbers[-1]

removed_numbers_sum = sum(removed_numbers)
print(removed_numbers_sum)
