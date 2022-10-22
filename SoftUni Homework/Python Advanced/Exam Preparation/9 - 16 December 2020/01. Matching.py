from collections import deque
males = list(map(int, input().split()))
females = deque(map(int, input().split()))
matches = 0

while males and females:
    male = males[-1]
    female = females[0]

    if male <= 0:
        males.pop()
        continue
    elif female <= 0:
        females.popleft()
        continue

    if male % 25 == 0:
        males.pop(), males.pop()
        continue
    elif female % 25 == 0:
        females.popleft(), females.popleft()
        continue

    if male == female:
        matches += 1
        males.pop()
        females.popleft()
    else:
        males[-1] -= 2
        females.popleft()

print(f'Matches: {matches}')
if males:
    print(f'Males left: {", ".join(str(x) for x in reversed(males))}')
else:
    print('Males left: none')
if females:
    print(f'Females left: {", ".join(str(x) for x in females)}')
else:
    print('Females left: none')
