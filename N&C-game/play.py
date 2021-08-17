from board import Board


def greetings():
    print('my honour', '\ndefine grid')


def play():
    turn = 0
    greetings()
    board = Board()
    board.building_grid(height=int(input()), width=int(input()))
    while True:
        turn += 1
        board.print_grid()
        coordinates = board.get_coordinates()
        board.update_grid(str(coordinates[0]), int(coordinates[1]), turn)


play()