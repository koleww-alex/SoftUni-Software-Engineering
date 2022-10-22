def operate(operator, *args):
    def add():
        return sum(args)

    def multiply():
        result = 1
        for num in args:
            result *= num
        return result

    def division():
        result = args[0]
        for i in range(1, len(args)):
            result /= args[i]
        return result

    def subtract():
        result = args[0]
        for i in range(1, len(args)):
            result -= args[i]
        return result

    if operator == '+':
        return add()
    elif operator == '*':
        return multiply()
    elif operator == '-':
        return subtract()
    elif operator == '/':
        return division()
