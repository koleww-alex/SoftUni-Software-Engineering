number = int(input())
sum_number = int(input())
total_sum = 0

while total_sum < number:
    total_sum += sum_number
    if total_sum >= number:
        print(total_sum)
        break
    sum_number = int(input())
