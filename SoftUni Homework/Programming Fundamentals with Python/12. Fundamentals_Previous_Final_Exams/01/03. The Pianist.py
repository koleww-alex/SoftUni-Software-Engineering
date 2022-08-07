number_of_pieces = int(input())
my_dict = {}
for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    if piece not in my_dict:
        my_dict[piece] = [composer, key]

while True:
    command = input().split("|")
    if "Stop" in command:
        break
    operation = command[0]

    if operation == "Add":
        piece, composer, key = command[1], command[2], command[3]
        if piece not in my_dict:
            my_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif operation == "Remove":
        piece = command[1]
        if piece in my_dict:
            my_dict.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif operation == "ChangeKey":
        piece, new_key = command[1], command[2]
        if piece in my_dict:
            my_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

print("\n".join(f"{key} -> Composer: {value[0]}, Key: {value[1]}" for key, value in my_dict.items()))
# Dictionaries
