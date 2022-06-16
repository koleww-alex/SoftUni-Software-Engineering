n = int(input())

total_sum = 0

for i in range(1, n + 1):
    current_letter = input()

    total_sum += ord(current_letter)

print(f"The sum equals: {total_sum}")
