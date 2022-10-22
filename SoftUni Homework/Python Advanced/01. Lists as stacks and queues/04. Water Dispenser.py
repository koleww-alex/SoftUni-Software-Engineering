from collections import deque
total_water = int(input())
queue = deque()
while True:
    people = input()
    if people == 'Start':
        break
    queue.append(people)

while queue:
    command = input().split()
    if len(command) == 1:
        person_in_queue = queue.popleft()
        used_liters = int(command[0])

        if total_water >= used_liters:
            total_water -= used_liters
            print(f'{person_in_queue} got water')
        else:
            print(f'{person_in_queue} must wait')
    else:
        refilled_liters = int(command[1])
        total_water += refilled_liters
print(f'{total_water} liters left')
