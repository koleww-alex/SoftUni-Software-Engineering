import sys

number = ""
min_number = sys.maxsize

while number != "Stop":
    number = input()
    if number == "Stop":
        break
    number = int(number)
    if number < min_number:
        min_number = number

print(min_number)
