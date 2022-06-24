list_of_integers = list(map(int, input().split("@")))
command = input()
length = 0
while command != "Love!":
    current_command = command.split()
    operation = current_command[0]
    index = int(current_command[1])
    length += index

    if operation == "Jump":
        if not length < len(list_of_integers):

            length = 0

        if list_of_integers[length] != 0:
            list_of_integers[length] -= 2
            if list_of_integers[length] == 0:
                print(f"Place {length} has Valentine's day.")
        else:
            print(f"Place {length} already had Valentine's day.")

    command = input()

house_count = [list_of_integers[i] for i in range(len(list_of_integers)) if list_of_integers[i] > 0]

print(f"Cupid's last position was {length}.")

if sum(list_of_integers) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(house_count)} places.")
