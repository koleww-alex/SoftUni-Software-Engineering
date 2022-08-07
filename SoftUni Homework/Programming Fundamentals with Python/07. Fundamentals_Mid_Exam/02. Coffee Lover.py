list_of_coffee = input().split()
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    operation = command[0]

    if operation == "Include":
        coffee = command[1]
        list_of_coffee.append(coffee)

    elif operation == "Remove":
        sub_operation = command[1]
        cnt = int(command[2])
        if cnt <= len(list_of_coffee):
            if sub_operation == "first":
                for _ in range(cnt):
                    list_of_coffee.pop(0)
            elif sub_operation == "last":
                for _ in range(cnt):
                    list_of_coffee.pop()
    elif operation == "Prefer":
        first_coffee = int(command[1])
        second_coffee = int(command[2])
        if 0 <= first_coffee < len(list_of_coffee) and 0 <= second_coffee < len(list_of_coffee):
            list_of_coffee[first_coffee], list_of_coffee[second_coffee] = \
                list_of_coffee[second_coffee], list_of_coffee[first_coffee]

    elif operation == "Reverse":
        list_of_coffee.reverse()
print("Coffees:")
print(" ".join(list_of_coffee))
