import sys
n = int(input())
biggest_number = -9223372036854775807
total_sum = 0

for i in range(1, n + 1):
    current_number = int(input())
    total_sum += current_number
    if current_number > biggest_number:
        biggest_number = current_number
total_sum -= biggest_number

if total_sum == biggest_number:
    print("Yes")
    print(f"Sum = {biggest_number}")
else:
    diff = abs(biggest_number - total_sum)
    print("No")
    print(f"Diff = {diff}")

