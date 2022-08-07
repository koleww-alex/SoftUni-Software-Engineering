def insert_space(secret_message, index):
    index = int(index)
    secret_message = secret_message[:index] + " " + secret_message[index:]
    print(secret_message)
    return secret_message


def reverse(secret_message, substring):
    if substring in secret_message:
        secret_message = secret_message.replace(substring, "", 1)
        reverse_substring = substring[::-1]
        secret_message += reverse_substring
        print(secret_message)
    else:
        print("error")
    return secret_message


def change_all(secret_message, substring, replacement):
    secret_message = secret_message.replace(substring, replacement)
    print(secret_message)
    return secret_message


secret_message = input()
command = input()

while command != "Reveal":
    current_command = command.split(":|:")
    operation = current_command[0]
    if operation == "InsertSpace":
        index = current_command[1]
        secret_message = insert_space(secret_message, index)
    elif operation == "Reverse":
        substring = current_command[1]
        secret_message = reverse(secret_message, substring)
    elif operation == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        secret_message = change_all(secret_message, substring, replacement)

    command = input()

print(f"You have a new text message: {secret_message}")
