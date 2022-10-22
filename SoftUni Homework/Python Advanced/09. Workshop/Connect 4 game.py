from termcolor import colored
from collections import deque

rows, cols = 6, 7
player_one_symbol = colored('◯', color='yellow')
player_two_symbol = colored('◯', color='red')
turn = deque([[colored('Yellow', color='yellow'), player_one_symbol], [colored('Red', color='red'), player_two_symbol]])
board = [['0'] * cols for _ in range(rows)]
is_winner = False
directions = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
)

while True:
    [print(f'[ {" ".join(board[row])} ]') for row in range(rows)]
    player_name, player_symbol = turn[0]
    try:
        col_chosen = int(input(f'\nPlayer {player_name}, please choose a column in the range (1 - 7): ')) - 1
    except ValueError:
        print(colored('Please insert a valid number!', color='red'))
        continue
    if not 0 <= col_chosen < cols:
        print(colored(f'Please, choose a valid column!', color='red'))
        continue

    row = 0
    if board[row][col_chosen] != '0':
        print(colored('This column is full!', color='red'))
        continue

    for _ in range(rows - 1):
        if board[row + 1][col_chosen] != '0':
            break
        row += 1

    board[row][col_chosen] = player_symbol
    for row in range(rows):
        for col in range(cols):
            spree = 0
            if board[row][col] == player_symbol:
                spree = 1
            else:
                continue
            for direction in directions:
                spree = 1
                r, c = row + direction[0], col + direction[1]
                for _ in range(3):
                    if not(0 <= r < rows and 0 <= c < cols):
                        break
                    elif board[r][c] != player_symbol:
                        break
                    spree += 1
                    r, c = r + direction[0], c + direction[1]

                if spree == 4:
                    is_winner = True

    if is_winner:
        print(colored('\n!!! GAME OVER !!!', color='magenta'))
        print(f'The winner is Player {player_name}')
        board[row][col_chosen] = player_symbol
        [print(f'[ {" ".join(board[row])} ]') for row in range(rows)]
        break

    turn.append(turn.popleft())
