stops = input()
while True:
    command = input().split()
    if "Travel" in command:
        break
    operation = command[0]

    if operation == "Add":
        stuff = command[1].split(":")
        index, string = stuff[1], stuff[2]
        index = int(index)
        if 0 <= index < len(stops):
            first_half = stops[:index]
            second_half = stops[index:]
            stops = first_half + string + second_half
        print(stops)

    elif operation == "Remove":
        stuff = command[1].split(":")
        start_index, end_index = stuff[1], stuff[2]
        start_index, end_index = int(start_index), int(end_index)
        if 0 <= start_index and end_index < len(stops):
            for ch in stops:
                if ch == stops[start_index]:
                    for _ in range(start_index, end_index + 1):
                        stops = stops.replace(stops[start_index], "", 1)
                    break
        print(stops)
    else:
        stuff = command[0].split(":")
        old_string, new_string = stuff[1], stuff[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)

print(f"Ready for world tour! Planned stops: {stops}")
