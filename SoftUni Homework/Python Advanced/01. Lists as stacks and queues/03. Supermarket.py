from collections import deque
queue = deque()
while True:
    name_of_person = input()
    if name_of_person == 'Paid':
        while queue:
            first_person_in_queue = queue.popleft()
            print(first_person_in_queue)
    elif name_of_person == 'End':
        break
    else:
        queue.append(name_of_person)

print(f'{len(queue)} people remaining.')
