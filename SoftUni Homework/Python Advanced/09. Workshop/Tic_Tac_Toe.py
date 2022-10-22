from termcolor import colored


def check_for_win():
    current_player, current_player_symbol = players_info[0]

    row = any([all(True if pos == current_player_symbol else False for pos in row) for row in board])

    primary_diagonal = all([board[i][i] == current_player_symbol for i in range(size)])

    col = any([all(True if board[r][c] == current_player_symbol else False for r in range(size)) for c in range(size)])

    secondary_diagonal = all([board[i][size - 1 - i] == current_player_symbol for i in range(size)])

    draw = all([all(True if board[r][c] in ['X', 'O'] else False for c in range(len(board))) for r in range(size)])

    if any([row, col, primary_diagonal, secondary_diagonal]):
        print(colored('\n!!! Game Over !!!', color='magenta'))
        print(f'{current_player} won!')
        print_board()
        exit()
    elif draw:
        print('The game ended in a draw!')
        print_board()
        exit()

    players_info.append(players_info.pop(0))


def execute_turn():
    try:
        current_player, current_player_symbol = players_info[0]
        pos_chosen = int(input(f'{current_player} please choose a free position [1 - 9]: ')) - 1
        if pos_chosen not in range(9):
            print(colored('Position out of range!', color='red'))
            execute_turn()

        if pos_chosen in pos_played:
            print(colored('This position is occupied!', color='red'))
            execute_turn()

        r, c = pos_chosen // 3, pos_chosen % 3
        board[r][c] = current_player_symbol
        pos_played.append(pos_chosen)
        check_for_win()
        print_board()
        execute_turn()

    except ValueError:
        print(colored('Please choose a valid position!', color='red'))
        execute_turn()


def print_board(start=False):
    if start:
        print('This is the numeration of the board:')
        [print(f"| {' | '.join(row)} |") for row in board]
        for row in range(len(board)):
            for col in range(len(board)):
                board[row][col] = ' '
    else:
        [print(f"| {' | '.join(row)} |") for row in board]


def start_game():
    player_one = input('Player one name: ')
    while True:
        player_two = input('Player two name: ')
        if player_one == player_two:
            print('Player names cannot be identical!')
            continue
        else:
            break
    while True:
        player_one_symbol = input(f"{player_one} would you like to play with 'X' or 'O'? ").upper()
        if player_one_symbol not in ['X', 'O']:
            print(colored('Please choose valid symbol!', color='red'))
            continue
        else:
            break
    player_two_symbol = 'O' if player_one_symbol == 'X' else 'X'

    players_info.append([player_one, colored(player_one_symbol, color='red')])
    players_info.append([player_two, colored(player_two_symbol, color='cyan')])
    print_board(start=True)
    execute_turn()
    print(f'{player_one} starts first!')


size = 3
board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, 10, 3)]
players_info = []
pos_played = []
start_game()
