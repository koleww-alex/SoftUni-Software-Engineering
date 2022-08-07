def add_stop(str_stops: str, i: int, s: str):
    if 0 <= i < len(stops):
        first_half = str_stops[:i]
        second_half = str_stops[i:]
        str_stops = first_half + s + second_half
        return str_stops
    return str_stops


def remove_stop(str_stops, start_index: int, end_index: int):
    if 0 <= start_index and end_index < len(stops):
        first_half = str_stops[:start_index]
        second_half = str_stops[end_index + 1:]
        str_stops = first_half + second_half
        return str_stops
    return str_stops


def switch(str_stops, old_string: str, new_string: str):
    if old_string in str_stops:
        return str_stops.replace(old_string, new_string)
    return str_stops


stops = input()
while True:
    command = input()
    if command == "Travel":
        break
    current_command = command.split(":")
    operation = current_command[0]

    if operation == "Add Stop":
        index, string = int(current_command[1]), current_command[2]
        stops = add_stop(stops, index, string)

    elif operation == "Remove Stop":
        first_index, second_index = int(current_command[1]), int(current_command[2])
        stops = remove_stop(stops, first_index, second_index)

    elif operation == "Switch":
        string, updated_string = current_command[1], current_command[2]
        stops = switch(stops, string, updated_string)

    print(stops)
print(f"Ready for world tour! Planned stops: {stops}")
