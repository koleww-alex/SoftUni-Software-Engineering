from collections import deque
working_bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())
total_honey = 0

while working_bees and nectar:

    if nectar[-1] >= working_bees[0]:
        operator = symbols.popleft()
        bee, nectar_collected = working_bees.popleft(), nectar.pop()
        if operator == '+':
            total_honey += abs(bee + nectar_collected)
        elif operator == '-':
            total_honey += abs(bee - nectar_collected)
        elif operator == '*':
            total_honey += abs(bee * nectar_collected)
        else:
            if bee > 0 and nectar_collected > 0:
                total_honey += abs(bee / nectar_collected)
    else:
        nectar.pop()

print(f'Total honey made: {total_honey}')

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
