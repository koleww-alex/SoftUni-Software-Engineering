from collections import deque
SIZE = 6
players = deque(input().split(', '))
matrix = [input().split() for _ in range(SIZE)]
skip_turn = {
    players[0]: False,
    players[1]: False,
}

while True:
    row, col = [int(x) for x in input().strip('()').split(', ')]

    if skip_turn[players[0]]:
        skip_turn[players[0]] = False
        players.append(players.popleft())
        continue

    if matrix[row][col] == 'E':
        print(f'{players[0]} found the Exit and wins the game!')
        break

    elif matrix[row][col] == 'T':
        print(f'{players[0]} is out of the game! The winner is {players[1]}.')
        break

    elif matrix[row][col] == 'W':
        print(f'{players[0]} hits a wall and needs to rest.')
        skip_turn[players[0]] = True

    players.append(players.popleft())
