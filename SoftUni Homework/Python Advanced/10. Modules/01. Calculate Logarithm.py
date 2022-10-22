from math import log
number = int(input())
base = input()

result = f'{log(number):.2f}' if base == 'natural' else f'{log(number, int(base)):.2f}'
print(result)
