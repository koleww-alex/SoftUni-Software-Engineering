import sys

number = ""
max_number = -sys.maxsize

while number != "Stop":
    number = input()
    if number == "Stop":
        break
    number = int(number)
    if number > max_number:
        max_number = number

print(max_number)
