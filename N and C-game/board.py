from prettytable import PrettyTable
import string


class Board:

    def __init__(self, row_names=[''], rows=[]):
        self.row_names = row_names 
        self.rows = rows

    def building_grid(self, height, width):
        count = 0
        for i in string.ascii_uppercase:
            if count < width:
                self.row_names.append(i)
                count += 1

        for j in range(height):
            row = ['' for _ in range(width + 1)]
            row[0] = j + 1
            self.rows.append(row)
        return self



    def check_for_winner(self, column, line, turn):
        column = string.ascii_uppercase.index(column) + 1
        letter = self.define_turn(turn)
        victory = False
        checking = True
        l_border = -2
        c_border = 2
        while checking:
            try:
                if self.rows[line + l_border][column - c_border] == letter and self.rows[line - l_border][column + c_border] == letter:
                    if self.rows[line + l_border][column - c_border] != self.rows[line - l_border][column + c_border]:
                        return not victory
                l_border += 1
                c_border -= 1
            except IndexError:
                continue
            if l_border >= 2 or c_border <= -2:
                    checking = not checking
        return victory

    
    def game_over(victory):
        if victory:
            return True

    def get_coordinates(self):
        print('print coordinates')
        coordinates = input().split()
        coordinates[1] = int(coordinates[1]) - 1
        return coordinates


    def define_turn(self, turn):
        if turn % 2 == 0:
            return 'O'
        else:
            return 'X'

    def update_grid(self, column, line, turn):
        column = string.ascii_uppercase.index(column) + 1
        letter = self.define_turn(turn)
        try:
            if self.rows[line][column] != '':
                raise Exception('Overlay exception')
            self.rows[line][column] = letter
        except Exception as e:
            print(e)
            coordinates = self.get_coordinates()
            self.update_grid(str(coordinates[0]), int(coordinates[1]), turn)

    def print_grid(self):
        grid = PrettyTable()
        grid.field_names = self.row_names
        grid.add_rows(self.rows)
        grid.align[''] = 'l'
        return print(grid)
