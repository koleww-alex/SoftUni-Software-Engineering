number = int(input())
total_sum = 0

for i in range(1, number + 1):
    current_number = int(input())
    total_sum += current_number

average = total_sum / number
print(f"{average:.2f}")
