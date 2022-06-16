def factorial(first, second):
    multipliers = 1
    for i in range(1, first):
        multipliers *= i
    first_sum = first * multipliers
    multipliers = 1
    for y in range(1, second):
        multipliers *= y
    second_sum = second * multipliers
    return f"{(first_sum / second_sum):.2f}"


first_number = int(input())
second_number = int(input())

print(factorial(first_number, second_number))
