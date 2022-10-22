SIZE = 8
matrix = [input().split() for _ in range(SIZE)]
w_pos, b_pos = [], []
turn = []
for row in range(SIZE):
    if 'w' in matrix[row]:
        w_pos = [row, matrix[row].index('w'), 'w']
    if 'b' in matrix[row]:
        b_pos = [row, matrix[row].index('b'), 'b']
turn.append(w_pos)
turn.append(b_pos)
pol = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', }

while True:
    row, col = turn[0][0], turn[0][1]
    if turn[0][2] == 'w':
        if [row - 1, col + 1] == [turn[1][0], turn[1][1]]:
            print(f'Game over! White win, capture on {pol[col + 1]}{SIZE - (row - 1)}.')
            break
        elif [row - 1, col - 1] == [turn[1][0], turn[1][1]]:
            print(f'Game over! White win, capture on {pol[col - 1]}{SIZE - (row - 1)}.')
            break
    else:
        if [row + 1, col + 1] == [turn[1][0], turn[1][1]]:
            print(f'Game over! Black win, capture on {pol[col + 1]}{SIZE - (row + 1)}.')
            break
        elif [row + 1, col - 1] == [turn[1][0], turn[1][1]]:
            print(f'Game over! Black win, capture on {pol[col - 1]}{SIZE - (row + 1)}.')
            break

    if turn[0][2] == 'w':
        turn[0][0] -= 1
    else:
        turn[0][0] += 1

    if turn[0][2] == 'b' and row == SIZE - 1:
        print(f'Game over! Black pawn is promoted to a queen at {pol[col]}{1}.')
        break
    elif turn[0][2] == 'w' and row == 0:
        print(f'Game over! White pawn is promoted to a queen at {pol[col]}{SIZE}.')
        break
    turn.append(turn.pop(0))
