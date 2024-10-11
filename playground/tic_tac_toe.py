all_spaces = list('123456789')
x, o, blank = 'X', 'O', ' '


def main():
    print("Welcome to Tic-Tac-Toe!")
    game_board = create_board()
    print(board_format(game_board))

    current_player, next_player = x, o

    while True:

        move = None
        while not valid_space(game_board, move):
            print(f"What is {current_player}'s next move?", end=' ')
            move = input()

        update_board(game_board, move, current_player)
        print(board_format(game_board))

        if is_winner(game_board, current_player):
            print(f"'{current_player}' won the game! 🎉")
            break
        elif is_tie(game_board):
            print("Game is tied. Good job to both of you!")
            break

        current_player, next_player = next_player, current_player


def create_board():
    board = {}
    for space in all_spaces:
        board[space] = blank

    return board


def board_format(board):
    return '''
        {}|{}|{}  1 2 3
        -+-+-
        {}|{}|{}  4 5 6
        -+-+-
        {}|{}|{}  7 8 9
    '''.format(board['1'], board['2'], board['3'], board['4'], board['5'], board['6'], board['7'], board['8'],
               board['9'])


def update_board(board, key, mark):
    board[key] = mark


def valid_space(board, space):
    return space in all_spaces and board[space] == blank


def is_winner(board, player):
    b, p = board, player
    return (b['1'] == b['2'] == b['3'] == p or  # across the top
            b['4'] == b['5'] == b['6'] == p or  # across the middle
            b['7'] == b['8'] == b['9'] == p or  # across the bottom
            b['1'] == b['4'] == b['7'] == p or  # down the left
            b['2'] == b['5'] == b['8'] == p or  # down the middle
            b['3'] == b['6'] == b['9'] == p or  # down the right
            b['1'] == b['5'] == b['9'] == p or  # diagonal from left
            b['3'] == b['5'] == b['7'] == p)


def is_tie(board):
    for value in board.values():
        if value == blank:
            return False
    return True


if __name__ == '__main__':
    main()
