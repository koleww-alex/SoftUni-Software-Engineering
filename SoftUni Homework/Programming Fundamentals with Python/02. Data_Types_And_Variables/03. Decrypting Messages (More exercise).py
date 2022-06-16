key_value = int(input())
number_of_iterations = int(input())

secret_message = ""

for _ in range(1, number_of_iterations + 1):
    current_chr = input()

    secret_chr = chr(ord(current_chr) + key_value)

    secret_message += secret_chr

print(secret_message)
