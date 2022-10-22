from collections import deque


def best_list_pureness(numbers: list, n: int):
    numbers = deque(numbers)
    best_pureness = [0, 0]
    for iteration in range(n + 1):
        pureness = 0
        for i in range(len(numbers)):
            pureness += numbers[i] * i

        if pureness > best_pureness[0]:
            best_pureness = [pureness, iteration]

        numbers.appendleft(numbers.pop())

    return f'Best pureness {best_pureness[0]} after {best_pureness[1]} rotations'


