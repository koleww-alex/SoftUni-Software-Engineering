from collections import deque

customers = deque(map(int, input().split(', ')))
taxis = list(map(int, input().split(', ')))
time_driven = 0
while customers and taxis:
    customer, taxi = customers[0], taxis[-1]

    if taxi >= customer:
        time_driven += customer
        customers.popleft(), taxis.pop()
    else:
        taxis.pop()

if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {time_driven} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(str(x) for x in customers)}')

