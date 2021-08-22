"""File that defines the "Board" class and all operations with the grid
"""

from prettytable import PrettyTable
import string


class Board:
    """Class implements all functions for creating the playing
    field, changing it and checking for a win or draw
    """

    def __init__(self, row_names=None, rows=None):
        """Initialisation of grid's markup"""
        if row_names is None:
            # Adding an empty string for sync of columns and lines
            row_names = ['']
        if rows is None:
            rows = []
        self.row_names = row_names 
        self.rows = rows


    def build_grid(self, width: str, height: str):
        # String method is required for column names
        count = 0
        for i in string.ascii_uppercase:
            if count < width:
                self.row_names.append(i)
                count += 1

        for j in range(height):
            # Filling the grid with empty strings
            row = ['' for _ in range(width + 1)]
            row[0] = str(j + 1)
            self.rows.append(row)
        return


    def get_diag(self):
        """Gets all diagonals in current grid"""
        diags = []
        # Size of column is equal to the rows in the grid
        column_size = len(self.rows)
        # Size of the line minus its number
        line_size = len(self.rows[0]) - 1
        # Calculatimg the diagonals of the symmetric or asymmetric grid
        if line_size == column_size:
            # Diags in both directions
            right_diag = []
            left_diag = []
            # Counter does not allow you to go outside the grid
            diag_count = 1
            for row in self.rows:
                if diag_count == line_size + 1:
                    break
                # Addendum of diags from opposite sides
                right_diag.append(row[diag_count])
                left_diag.append(row[-diag_count])
                diag_count += 1
            # Getting the matrix with all diags
            diags = [right_diag] + [left_diag]
        elif line_size < column_size:
            for diag in range(column_size):
                if column_size - diag < line_size:
                    break
                right_diag = []
                left_diag = []
                diag_count = 1
                # Additional counter for enumeration of lines
                row = diag
                # Cycle is a counter for the element's line position
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
                # Resetting diag_count 
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


    @staticmethod
    def check_diag(diags, letter, win_row_size):
        """Checks diagonals for wincondition
        
        Args:
        diags (list): all diagonals in the grid
        letter (str): "X" or "O"
        win_row_size (int): number of consecutive characters for a win

        """
        for diag in diags:
            win_diag_count = 0
            for elem in diag:
                if elem == letter:
                    win_diag_count += 1
                else:
                    win_diag_count = 0
                if win_diag_count == win_row_size:
                    return True     
        return False


    def check_vertical_and_flat(self, column, letter, win_row_size):
        """Checks vertical and horisontal axes for a wincondition
        
        Args:
        column (int): number of a column
        letter (str): "X" or "O"
        win_row_size (int): number of consecutive characters for a win
        
        """
        win_column_count = 0
        win_line_count = 0
        for row in self.rows:
            for elem in row:
                # Line examination
                # Checking symbol for matching the target
                if elem == letter:
                    win_line_count += 1
                else:
                    win_line_count = 0
                if win_line_count == win_row_size:
                    return True 
            win_line_count = 0
            # Column examination
            # Checking symbol for matching the target
            if row[column] == letter:
                win_column_count += 1
            else:
                win_column_count = 0
            if win_column_count == win_row_size:
                return True
        return False


    def check_for_winner(self, column, turn, win_row_size):
        """Checks for a winconditions in all directions
        
        Args:
        column (int): number of a column
        letter (str): "X" or "O"
        win_row_size (int): number of consecutive characters for a win
        
        """
        column = string.ascii_uppercase.index(column) + 1
        letter = self.define_turn(turn)
        victory = False
        diags = self.get_diag()
        if self.check_vertical_and_flat(column, letter, win_row_size):
            return not victory
        if self.check_diag(diags, letter, win_row_size):
            return not victory
        return victory


    def check_for_draw(self):
        """Checks grid to be totally filled"""
        for row in self.rows:
            for elem in row:
                if elem == '':
                    return False
        return True


    def get_coordinates(self):
        # Catching possible input errors
        checking = True
        while checking:
            #Getting coordinates of player's move
            print('input coordinates to make your move')
            coordinates = input().split()
            if len(coordinates) != 2:
                print('Incorrect letter of a column or number of a line')
                continue
            x_coordinate = coordinates[0]
            y_coordinate = coordinates[1]
            if self.check_coordinates(x_coordinate, y_coordinate):
                y_coordinate = int(y_coordinate) - 1
                checking = not checking
        return x_coordinate, y_coordinate

    def check_coordinates(self, x:str, y:str):
        """Checks whether the first element is suitable letter and
        second element is in the grid's borders
        """
        if (x not in self.row_names or not y.isdigit() or
            int(y) > len(self.rows) or int(y) <= 0):
                print('Incorrect letter of a column or number of a line')
                return False
        return True


    def define_player(self, p1:str, p2:str, turn:int):
        """Defines whose turn it is"""
        if turn % 2 == 0:
            return p2
        else:
            return p1


    @staticmethod
    def define_turn(turn):
        if turn % 2 == 0:
            return 'O'
        else:
            return 'X'


    def update_grid(self, column, line, turn):
        """Checks for errors in player's input
        
        Args:
        column (str): letter of a column
        line (int): number of a line
        turn(int): number of a turn
        
        """
        # Converting a letter to a number in alphabetical order
        column = string.ascii_uppercase.index(column) + 1
        # Defining the letter
        letter = self.define_turn(turn)
        # Adding an element to the grid
        try:
            # Checking for overlay
            if self.rows[line][column] != '':
                raise Exception('Overlay exception')
            self.rows[line][column] = letter
        # Repeating the function if necessary
        except Exception as e:
            print('That place is occupied')
            coordinates = self.get_coordinates()
            self.update_grid(str(coordinates[0]), int(coordinates[1]), turn)


    def print_grid(self):
        """Converts and prints the grid in "PrettyTable" view"""
        grid = PrettyTable()
        # Getting letters for column names
        grid.field_names = self.row_names
        # Adding the matrix with new data
        grid.add_rows(self.rows)
        # lign the numbering of lines
        grid.align[''] = 'l'
        return print(grid)
