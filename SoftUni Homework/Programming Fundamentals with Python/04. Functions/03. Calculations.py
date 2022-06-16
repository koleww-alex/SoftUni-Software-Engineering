def operations(f_number, s_number):
    result = 0

    if operation == "subtract":
        result = f_number - s_number
    elif operation == "divide":
        result = f_number // s_number
    elif operation == "multiply":
        result = f_number * s_number
    else:
        result = f_number + s_number
    return result


operation = input()
first_number = int(input())
second_number = int(input())

print(operations(first_number, second_number))
