from collections import deque

string = input().split()
operations = ['+', '-', '/', '*']
numbers = deque()
result = 0
iterations = 0
for element in string:

    if element in operations:
        iterations += 1
        if element == '+':
            for _ in range(len(numbers)):
                result += numbers.popleft()
        elif element == '-':
            if result == 0:
                result += numbers.popleft()
            for i in range(len(numbers)):
                result -= numbers.popleft()
        elif element == '*':
            if iterations == 1:
                result = numbers.popleft()
            for i in range(len(numbers)):
                result *= numbers.popleft()
        elif element == '/':
            if iterations == 1:
                result = numbers.popleft()
            for i in range(len(numbers)):
                result //= numbers.popleft()
    else:
        numbers.append(int(element))

print(result)
