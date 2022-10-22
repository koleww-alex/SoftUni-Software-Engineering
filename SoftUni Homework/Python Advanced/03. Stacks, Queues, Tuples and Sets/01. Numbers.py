first_set, second_set = set(input().split()), set(input().split())
N = int(input())

for _ in range(N):
    command = input()

    if 'Add First' in command:
        command = command.split()
        numbers = command[2:]
        first_set = first_set.union(numbers)

    elif 'Add Second' in command:
        command = command.split()
        numbers = command[2:]
        second_set = second_set.union(numbers)

    elif 'Remove First' in command:
        command = command.split()
        numbers = command[2:]
        for num in numbers:
            if num in first_set:
                first_set.remove(num)

    elif 'Remove Second' in command:
        command = command.split()
        numbers = command[2:]
        for num in numbers:
            if num in second_set:
                second_set.remove(num)

    elif 'Check Subset' in command:
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print('True')
        else:
            print('False')

# first_set = list(map(int, first_set))
# second_set = list(map(int, second_set))

print(', '.join(map(str, sorted(list(map(int, first_set))))))
print(', '.join(map(str, sorted(list(map(int, second_set))))))
