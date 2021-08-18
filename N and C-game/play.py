from board import Board


def greetings():
    print('my honour', '\ndefine grid')

def play():
    turn = 0
    greetings()
    board = Board()
    board.building_grid(height=int(input()), width=int(input()))
    game = True
    while game:
        turn += 1
        print(board.rows)
        board.print_grid()
        coordinates = board.get_coordinates()
        board.update_grid(coordinates[0], coordinates[1], turn)
        print(board.rows[coordinates[1]])
        if board.check_for_winner(coordinates[0], coordinates[1], turn):
            board.print_grid()
            print('GAME OVER')
            game = not game


play()