numbers = int(input())

total_even = 0
total_odd = 0

even_current_number = 0
odd_current_number = 0

for i in range(1, numbers + 1):
    current_number = int(input())
    if i % 2 == 0:
        even_current_number = current_number
        total_even += even_current_number
    else:
        odd_current_number = current_number
        total_odd += odd_current_number

diff = abs(total_even - total_odd)

if total_even == total_odd:
    print("Yes")
    print(f"Sum = {total_even}")
else:
    print("No")
    print(f"Diff = {diff}")
