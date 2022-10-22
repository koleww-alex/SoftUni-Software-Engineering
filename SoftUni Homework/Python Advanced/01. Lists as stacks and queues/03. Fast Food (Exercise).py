from collections import deque
total_food = int(input())
queue = deque(list(map(int, input().split())))
left_orders = []
print(max(queue))

while queue:
    if queue:
        first_order = queue.popleft()
        if total_food >= first_order:
            total_food -= first_order
        else:
            left_orders.append(first_order)
            for _ in range(len(queue)):
                left_orders.append(queue.popleft())

left_orders = [str(el) for el in left_orders]
if not left_orders:
    print('Orders complete')
else:
    print(f'Orders left: {" ".join(left_orders)}')
