list_of_elements = input().split()
command = input()
number_of_moves = 0

did_we_won = False

while command != "end":
    command = command.split()
    number_of_moves += 1
    first_index = int(command[0])
    second_index = int(command[1])

    if first_index == second_index or first_index < 0 or first_index >= len(list_of_elements) or second_index < 0 or \
            second_index >= len(list_of_elements):

        middle_of_the_list = len(list_of_elements) // 2
        list_of_elements.insert(middle_of_the_list, f"-{number_of_moves}a")
        list_of_elements.insert(middle_of_the_list, f"-{number_of_moves}a")
        print("Invalid input! Adding additional elements to the board")
        command = input()
        continue
    if list_of_elements[first_index] == list_of_elements[second_index]:
        print(f"Congrats! You have found matching elements - {list_of_elements[first_index]}!")
        if second_index == 0:
            list_of_elements.pop(first_index)
            list_of_elements.pop(second_index)
        else:
            list_of_elements.pop(first_index)
            list_of_elements.pop(second_index - 1)

    elif list_of_elements[first_index] != list_of_elements[second_index]:
        print("Try again!")

    if len(list_of_elements) == 0:
        print(f"You have won in {number_of_moves} turns!")
        did_we_won = True
        break

    command = input()

list_of_strings = [str(number) for number in list_of_elements]

if not did_we_won:
    print("Sorry you lose :(")
    print(" ".join(list_of_strings))
