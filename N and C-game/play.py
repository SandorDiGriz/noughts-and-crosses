from board import Board

def define_winner(turn):
    if turn % 2 == 0:
        return 
    else:
        return 

def play():
    print('Welcome, strangers!', '\nPlease, define your grid (''3 3'' for example)')
    grid_size = list(map(int, input().split()))
    height, width = grid_size[0], grid_size[1]
    board = Board()
    board.building_grid(height, width)
    turn = 0
    win_row_size = max(grid_size)

    print('P1, introduce yourself')
    P1 = input()
    print('P2, introduce yourself')
    P2 = input()

    winner = None
    game = True
    while game:
        turn += 1
        board.print_grid()
        coordinates = board.get_coordinates()
        board.update_grid(coordinates[0], coordinates[1], turn)
        if board.check_for_winner(coordinates[0], coordinates[1], turn, win_row_size):
            board.print_grid()
            winner = P2 if turn % 2 == 0 else P1
            print('GAME OVER', winner, 'wins')
            game = not game
            


play()