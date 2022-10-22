from collections import deque

bowls_of_ramen = deque(map(int, input().split(', ')))
customers = deque(map(int, input().split(', ')))

while bowls_of_ramen and customers:
    last_bowl = bowls_of_ramen[-1]
    first_customer = customers[0]

    if last_bowl == first_customer:
        bowls_of_ramen.pop(), customers.popleft()

    elif last_bowl > first_customer:
        bowls_of_ramen[-1] -= first_customer
        customers.popleft()

    elif first_customer > last_bowl:
        customers[0] -= last_bowl
        bowls_of_ramen.pop()


if not customers:
    print('Great job! You served all the customers.')
    if bowls_of_ramen:
        print(f'Bowls of ramen left: {", ".join(str(x) for x in bowls_of_ramen)}')
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f'Customers left: {", ".join(str(x) for x in customers)}')
