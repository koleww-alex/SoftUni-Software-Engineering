numbers = int(input())

left_current_number = 0
right_current_number = 0
total_left = 0
total_right = 0

for i in range(numbers):
    left_current_number = int(input())
    total_left += left_current_number

for i in range(numbers):
    right_current_number = int(input())
    total_right += right_current_number

diff = abs(total_left - total_right)

if total_left == total_right:
    print(f"Yes, sum = {total_left}")
else:
    print(f"No, diff = {diff}")

