from Units import fibonacci_calc

fibonacci_list = []
while True:
    command = input().split()
    if 'Stop' in command:
        break

    if 'Create' in command:
        n = int(command[2])
        fibonacci_list = fibonacci_calc.create_sequence(n)
        print(' '.join(str(x) for x in fibonacci_list))
    elif 'Locate' in command:
        number = int(command[1])
        if number in fibonacci_list:
            print(f'The number - {number} is at index {fibonacci_list.index(number)}')
        else:
            print(f'The number {number} is not in the sequence')
