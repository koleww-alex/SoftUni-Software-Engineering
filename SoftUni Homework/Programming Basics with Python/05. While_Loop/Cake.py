cake_lenght = int(input())
cake_width = int(input())
command = input()
slices_taken = 0

slices = cake_lenght * cake_width

while command != "STOP":
    slices_taken += int(command)

    if slices_taken > slices:
        slices_left = False
        break

    command = input()

if command == "STOP":
    slices_left = slices - slices_taken
    print(f"{slices_left} pieces are left.")
else:
    slices_needed = slices_taken - slices
    print(f"No more cake left! You need {slices_needed} pieces more.")
