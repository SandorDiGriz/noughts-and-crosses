"""Executive file running the game importing 'Board' parameters"""

from board import Board


def play():
    """Gets players' data and runs the game"""
    print('\nWelcome, strangers!\n', '\nPlease, define your grid  \
        \n''3 3'' for example')
    print('\nRemember, that you inputting the width first!')
    # Importing 'Board' class settings
    board = Board()
    # Setting size of grid
    grid_size = list(map(int, input().split()))
    width, height = grid_size[0], grid_size[1]
    board.build_grid(width, height)
    board.print_grid()
    print('You will need to choose a column and a row number to make a move'
        '\nGood luck!')
    # Setting turns' counter
    turn = 0
    # Defining size of a win row
    win_row_size = min(grid_size)

    print('"X" player, introduce yourself')
    player_1 = input()
    print('"O" player, introduce yourself')
    player_2 = input()
    winner = None
    # Setting game flag
    game = True
    while game:
        turn += 1
        board.print_grid()
        print(board.define_player(player_1, player_2, turn) + ',' '\nYour turn!')
        # Getting player's move coordinates
        x_coordinate, y_coordinate = board.get_coordinates()
        board.update_grid(x_coordinate, y_coordinate, turn)
        if board.check_for_winner(x_coordinate, turn, win_row_size):
            board.print_grid()
            winner = player_2 if turn % 2 == 0 else player_1
            print('GAME OVER')
            print(winner, 'wins')
            game = not game
        elif board.check_for_draw():
            board.print_grid()
            print('GAME OVER')
            print('Friendship wins')
            game = not game
