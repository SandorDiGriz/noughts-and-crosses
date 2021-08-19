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

    def get_diag(self):
        diags = []
        right_diag = []
        left_diag = []
        right_diag_count = 1
        left_diag_count = len(self.rows[0]) - 1
        for row in self.rows:
            if right_diag_count == len(self.rows[0]) or left_diag_count < 0:
                break
            right_diag.append(row[right_diag_count])
            left_diag.append(row[left_diag_count])
            right_diag_count += 1
            left_diag_count -= 1
        diags = [right_diag] + [left_diag]
        return diags


    def check_for_winner(self, column, line, turn, win_row_size):
        column = string.ascii_uppercase.index(column) + 1
        letter = self.define_turn(turn)
        victory = False
        win_column_count = 0
        diag = self.get_diag()
        for row in self.rows:
            win_line_count = 0
            if row[column] == letter:
                win_column_count += 1
                if win_column_count == win_row_size:
                    return not victory
            for elem in row:
                if elem == letter:
                    win_line_count += 1
                    if win_line_count == win_row_size:
                        return not victory
        for i in diag:
            win_diag_count = 0
            for j in i:
                if j == letter:
                    win_diag_count += 1
                    if win_diag_count == win_row_size:
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
