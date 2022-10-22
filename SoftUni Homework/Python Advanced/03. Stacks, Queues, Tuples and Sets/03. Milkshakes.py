from collections import deque

chocolate = list(map(int, input().split(', ')))
milk_cups = deque(map(int, input().split(', ')))
milk_shakes = 0

while milk_cups and chocolate and milk_shakes < 5:
    flag = False

    if chocolate[-1] <= 0:
        chocolate.pop()
        flag = True

    if milk_cups[0] <= 0:
        milk_cups.popleft()
        flag = True

    if flag:
        continue

    if chocolate[-1] == milk_cups[0]:
        milk_shakes += 1
        chocolate.pop()
        milk_cups.popleft()

    else:
        milk_cups.append(milk_cups.popleft())
        chocolate[-1] -= 5

if milk_shakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolate:
    print(f'Chocolate: {", ".join(str(x) for x in chocolate)}')
else:
    print('Chocolate: empty')

if milk_cups:
    print(f'Milk: {", ".join(str(x) for x in milk_cups)}')
else:
    print('Milk: empty')
