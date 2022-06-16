number_of_wagons = int(input())
wagons = [0] * number_of_wagons

command = input()

while command != "End":
    current_command = command.split()

    operation = current_command[0]

    if operation == "add":
        people = int(current_command[1])
        wagons[-1] += people
    elif operation == "insert":

        index = int(current_command[1])
        people = int(current_command[2])
        wagons[index] += people

    elif operation == "leave":
        index = int(current_command[1])
        people = int(current_command[2])
        wagons[index] -= people

    command = input()

print(wagons)
