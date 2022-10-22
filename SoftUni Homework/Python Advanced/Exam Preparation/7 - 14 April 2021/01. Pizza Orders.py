from collections import deque

pizza_orders = deque(map(int, input().split(', ')))
employees = list(map(int, input().split(', ')))
pizza_made = 0
while employees and pizza_orders:
    pizza = pizza_orders[0]

    if pizza <= 0 or pizza > 10:
        pizza_orders.popleft()
        continue
    employee = employees.pop()

    if employee >= pizza:
        pizza_orders.popleft()
        pizza_made += pizza

    else:
        pizza_orders[0] -= employee
        pizza_made += employee

if not pizza_orders:
    print(f'All orders are successfully completed!')
    print(f'Total pizzas made: {pizza_made}')
    print(f'Employees: {", ".join(str(x) for x in employees)}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(str(x) for x in pizza_orders)}')
