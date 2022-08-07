secret_message = input()
command = input()
while command != "Reveal":
    current_command = command.split(":|:")
    operation = current_command[0]

    if operation == "InsertSpace":
        index = int(current_command[1])
        secret_message = secret_message[:index] + " " + secret_message[index:]
        print(secret_message)
    elif operation == "Reverse":
        substring = current_command[1]
        if substring in secret_message:
            secret_message = secret_message.replace(substring, "", 1)
            reverse_substring = substring[::-1]
            secret_message += reverse_substring
            print(secret_message)
        else:
            print("error")
    elif operation == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        secret_message = secret_message.replace(substring, replacement)
        print(secret_message)

    command = input()

print(f"You have a new text message: {secret_message}")
