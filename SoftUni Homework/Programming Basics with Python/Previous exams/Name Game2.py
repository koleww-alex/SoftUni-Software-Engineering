from sys import maxsize

command = input()

max_number = -maxsize

name = ""

while command != "Stop":
    points = 0
    for ch in command:
        number = int(input())
        ascii_number = ord(ch)
        if number == ascii_number:
            points += 10
        else:
            points += 2
    if points >= max_number:
        max_number = points
        name = command

    command = input()

print(f"The winner is {name} with {max_number} points!")


