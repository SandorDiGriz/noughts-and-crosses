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
        try:
            if self.rows[line + 1][column + 1] == letter and self.rows[line + 2][column + 2] == letter:
                    return not victory
            elif self.rows[line - 1][column - 1] == letter and self.rows[line - 2][column - 2] == letter:
                    return not victory
            elif self.rows[line - 1][column + 1] == letter and self.rows[line - 2][column + 2] == letter:
                    return not victory
            elif self.rows[line + 2][column - 1] == letter and self.rows[line - 2][column + 1] == letter:
                    return not victory
            elif self.rows[line - 1][column - 1] == letter and self.rows[line + 1][column + 1] == letter:
                    return not victory
        except IndexError:
            pass
        if len(self.rows) > line:
            if self.rows[line - 1][column] == letter and self.rows[line - 2][column] == letter:
                return not victory
            elif self.rows[line - 1][column] == letter and self.rows[line + 1][column] == letter:
                return not victory
        elif len(self.rows) < line:
            if self.rows[line + 1][column] == letter and self.rows[line + 2][column] == letter:
                return not victory

        if len(self.rows[line]) > column:
            if self.rows[line][column - 1] == letter and self.rows[line][column - 2] == letter:
                return not victory
        elif len(self.rows[line]) < column:
            if self.rows[line][column + 1] == letter and self.rows[line][column + 2] == letter:
                return not victory
        elif self.rows[line][column - 1] == letter and self.rows[line][column + 1] == letter:
            return not victory
        
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
