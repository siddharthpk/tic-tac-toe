import math

class TicTacToe():
    # Constructor to initialize the board and the current winner
    def __init__(self) -> None:
        self.board  = self.make_board()
        self.current_winner = None
    
    # Returns the board boundaries  
    @staticmethod
    def make_board():
        return [ ' ' for _ in range(9)]
    
    # Prints the board, uses make_board()
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    # Prints the board's numbers for visualization
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range((j*3),(j+1)*3)] for j in range(3)]
        for row in number_board:
            print(print('| ' + ' | '.join(row) + ' |'))

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            
            return True
        return False
    
    def winner(self, square, letter):
        # Check the row
        row_idx = math.floor(square/3)
        row = self.board[row_idx*3:(row_idx+1)*3]

        # Print winning tiles row
        if all([s == letter] for s in row):
            return True
        col_idx = square%3
        column = [self.board[col_idx+i*3] for i in range(3)]

        # Print winner tiles column
        if all([s == letter] for s in column):
            return True
        
        # Check if winner tiles on a diagnol
        if square%2 == 0:
            diag1 = [self.board[i] for i in [0,4,8]]
            # Print first Diagonal
            if all([s == letter] for s in diag1):
                return True
            
            diag2 = [self.board[i] for i in [2,4,6]]
            # Print second Diagonal
            if all([s == letter] for s in diag2):
                return True
            
        return False
    
    
