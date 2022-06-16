command = input()

sum_prime_numbers = 0
sum_non_prime_numbers = 0

while command != "stop":
    numbers = int(command)

    if numbers < 0:
        print("Number is negative.")
        command = input()
        continue
    is_non_prime_number = False
    for i in range(2, numbers):
        if numbers % i == 0:
            is_non_prime_number = True
    if is_non_prime_number:
        sum_non_prime_numbers += numbers
    else:
        sum_prime_numbers += numbers
    command = input()

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")
