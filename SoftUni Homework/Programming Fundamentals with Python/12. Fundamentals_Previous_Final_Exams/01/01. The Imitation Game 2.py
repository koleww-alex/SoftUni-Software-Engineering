encrypted_message = input()
while True:
    command = input().split("|")
    if "Decode" in command:
        break
    operation = command[0]

    if operation == "Move":
        number_of_letters_to_move = int(command[1])
        i = 0
        for ch in encrypted_message:
            if i == number_of_letters_to_move:
                break
            encrypted_message += ch
            encrypted_message = encrypted_message.replace(ch, "", 1)
            i += 1

    elif operation == "Insert":
        index = int(command[1])
        ch = command[2]
        first_half = encrypted_message[:index]
        second_half = encrypted_message[index:]
        first_half += ch
        encrypted_message = first_half + second_half

    elif operation == "ChangeAll":
        old_ch = command[1]
        new_ch = command[2]
        encrypted_message = encrypted_message.replace(old_ch, new_ch)

print(f"The decrypted message is: {encrypted_message}")
# Text Processing
