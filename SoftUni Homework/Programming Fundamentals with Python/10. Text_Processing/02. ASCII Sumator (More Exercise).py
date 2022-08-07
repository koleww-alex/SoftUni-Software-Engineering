lower_border = ord(input())
upper_border = ord(input())
string = input()
total_sum = 0

for ch in string:
    if lower_border < ord(ch) < upper_border:
        total_sum += ord(ch)

print(total_sum)
