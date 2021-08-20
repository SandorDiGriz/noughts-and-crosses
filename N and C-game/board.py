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
        column_size = len(self.rows)
        line_size = len(self.rows[0]) - 1
        if line_size == column_size:
            right_diag = []
            left_diag = []
            diag_count = 1
            for row in self.rows:
                if diag_count == line_size + 1:
                    break
                right_diag.append(row[diag_count])
                left_diag.append(row[-diag_count])
                diag_count += 1
            diags = [right_diag] + [left_diag]
        elif line_size < column_size:
            for diag in range(column_size):
                if column_size - diag < line_size:
                    break
                right_diag = []
                left_diag = []
                diag_count = 1
                row = diag
                for _ in range(line_size):
                    right_diag.append(self.rows[row][diag_count])
                    left_diag.append(self.rows[row][-diag_count])
                    diag_count += 1
                    row += 1
                diags.append(right_diag)
                diags.append(left_diag)
        else:
            diag_count, line_count = 1, 1
            for diag in range(line_size):
                diag_count = line_count
                if line_size - diag < column_size:
                    break
                right_diag = []
                left_diag = []
                row = 0
                for _ in range(column_size):
                    right_diag.append(self.rows[row][diag_count])
                    left_diag.append(self.rows[row][-diag_count])
                    diag_count += 1
                    row += 1
                line_count += 1
                diags.append(right_diag)
                diags.append(left_diag)
        return diags

    def check_diag(self, diags, letter, win_row_size):
        for i in diags:
            win_diag_count = 0
            for j in i:
                if j == letter:
                    win_diag_count += 1
                else:
                    win_diag_count = 0
                if win_diag_count == win_row_size:
                    return True     
        return False

    def check_vertical_and_flat(self, column, letter, win_row_size):
        win_column_count = 0
        for row in self.rows:
            for elem in row:
                if elem == letter:
                    win_line_count += 1
                else:
                    win_line_count = 0
                if win_line_count == win_row_size:
                    return True 
            win_line_count = 0
            if row[column] == letter:
                win_column_count += 1
            else:
                win_column_count = 0
            if win_column_count == win_row_size:
                return True
        return False

    def check_for_winner(self, column, line, turn, win_row_size):
        column = string.ascii_uppercase.index(column) + 1
        letter = self.define_turn(turn)
        victory = False
        diags = self.get_diag()
        if self.check_vertical_and_flat(column, letter, win_row_size):
            return not victory
        if self.check_diag(diags, letter, win_row_size):
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
