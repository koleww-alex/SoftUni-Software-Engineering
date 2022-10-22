number_of_operations = int(input())
stack = []
for _ in range(number_of_operations):
    command = input()

    if command[0] == '1':
        current_command = command.split()
        number = current_command[1]
        stack.append(int(number))
    if stack:
        if command[0] == '2':
            stack.pop()
        elif command[0] == '3':
            print(max(stack))
        elif command[0] == '4':
            print(min(stack))

reversed_stack = [str(stack[i]) for i in range(len(stack) - 1, -1, -1)]
print(', '.join(reversed_stack))
