command = input()
name_lenght = len(command)
points = 0

for _ in range(1, name_lenght + 1):
    number = int(input())
    for ch in command:
        if number == ord(ch):
            points += 10
        else:
            points += 2


# print(f"The winner is {името на победителя} with {точките на победителя} points!")


