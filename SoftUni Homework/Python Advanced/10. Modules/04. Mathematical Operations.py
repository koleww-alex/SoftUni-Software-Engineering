from Units import calculations
first_num, operation, second_num = input().split()


def calculate(num_one, operator, num_two):
    if operator == '+':
        return calculations.add(num_one, num_two)

    elif operator == '-':
        return calculations.subtract(num_one, num_two)

    elif operator == '/':
        return calculations.divide(num_one, num_two)

    elif operator == '*':
        return calculations.multiply(num_one, num_two)

    elif operator == '^':
        return calculations.degree(num_one)


print(f'{calculate(float(first_num), operation, float(second_num)):.2f}')
