from collections import deque
queue_of_players = deque(input().split())
number_of_tosses = int(input())

while len(queue_of_players) > 1:
    for i in range(1, number_of_tosses + 1):
        if number_of_tosses == i:
            first_to_leave_game = queue_of_players.popleft()
            print(f'Removed {first_to_leave_game}')
        else:
            first_person_in_queue = queue_of_players.popleft()
            queue_of_players.append(first_person_in_queue)

winner = queue_of_players.popleft()
print(f'Last is {winner}')


