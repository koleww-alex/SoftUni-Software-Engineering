number_of_iterations = int(input())
storage = {}
for _ in range(number_of_iterations):
    info = input().split("|")
    car, mileage, fuel = info
    if car not in storage:
        storage[car] = [int(mileage), int(fuel)]

command = input()
while command != "Stop":
    current_command = command.split(" : ")
    operation = current_command[0]

    if operation == "Drive":
        car, distance, fuel = current_command[1], int(current_command[2]), int(current_command[3])
        storage[car][0] = int(storage[car][0])
        storage[car][1] = int(storage[car][1])
        if storage[car][1] >= fuel:
            storage[car][0] += distance
            storage[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if storage[car][0] >= 100_000:
                del storage[car]
                print(f"Time to sell the {car}!")
        else:
            print("Not enough fuel to make that ride")

    elif operation == "Refuel":
        car, fuel = current_command[1], int(current_command[2])
        storage[car][1] = int(storage[car][1])
        if storage[car][1] + fuel > 75:
            refill = 75 - storage[car][1]
            storage[car][1] = 75
        else:
            refill = fuel
            storage[car][1] += refill
        print(f"{car} refueled with {refill} liters")

    elif operation == "Revert":
        car, kilometers = current_command[1], int(current_command[2])
        storage[car][0] -= kilometers
        if storage[car][0] < 10_000:
            storage[car][0] = 10_000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for car, info in storage.items():
    print(f"{car} -> Mileage: {info[0]} kms, Fuel in the tank: {info[1]} lt.")
