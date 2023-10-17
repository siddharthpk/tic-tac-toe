import math
import time
from player import HumanPlayer, ComputerPlayer, AIComputerPlayer

class TicTacToe():
    """
    A class representing the Tic Tac Toe game.

    Attributes:
    - board (list): A list representing the Tic Tac Toe board.
    - current_winner (str): The current winner of the game.

    Methods:
    - __init__(self): Initializes the board and the current winner.
    - make_board(): Returns the board boundaries.
    - print_board(self): Prints the Tic Tac Toe board.
    - print_board_nums(): Prints the Tic Tac Toe board's numbers for visualization.
    - make_move(self, square, letter): Makes a move on the Tic Tac Toe board.
    - winner(self, square, letter): Determines if a player has won the game.
    - empty_squares(self): Returns the empty squares on the board.
    - num_empty_squares(self): Returns the number of empty squares on the board.
    - available_moves(self): Returns the available moves on the board.
    """

    

    def __init__(self) -> None:
        self.board  = self.make_board()
        self.current_winner = None
    
    @staticmethod
    def make_board():
        """
        Returns a list representing the Tic Tac Toe board.

        Returns:
        - list: A list representing the Tic Tac Toe board.
        """
        return [ ' ' for _ in range(9)]
    
    def print_board(self):
        """
        Prints the Tic Tac Toe board.
        """
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        """
        Prints the Tic Tac Toe board's numbers for visualization.
        """
        number_board = [[str(i) for i in range((j*3),(j+1)*3)] for j in range(3)]
        for row in number_board:
            print(print('| ' + ' | '.join(row) + ' |'))

    def make_move(self, square, letter):
        """
        Makes a move on the Tic Tac Toe board.

        Args:
        - square (int): The index of the square to make a move on.
        - letter (str): The letter ('X' or 'O') to make a move with.

        Returns:
        - bool: True if the move is valid, False otherwise.
        """
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            
            return True
        return False
    
    def winner(self, square, letter):
        """
        Determines if a player has won the game by checking the row, column, and diagonal containing the given square.

        Args:
        - square (int): The index of the square to check.
        - letter (str): The letter ('X' or 'O') of the player to check for a win.

        Returns:
        - bool: True if the player has won, False otherwise.
        """
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
    
    def empty_squares(self):
        """
        Returns the empty squares on the board.

        Returns:
        - bool: True if there are empty squares on the board, False otherwise.
        """
        return ' ' in self.board

    def num_empty_squares(self):
        """
        Returns the number of empty squares on the board.

        Returns:
        - int: The number of empty squares on the board.
        """
        return self.board.count(' ')
    
    def available_moves(self):
        """
        Returns the available moves on the board.

        Returns:
        - list: A list of available moves on the board.
        """
        return [ i for i, x in enumerate(self.board) if x == " "] 
        # enumerate() allow to iterate through the object and keep track of the index of each element

def play(game, X_Player, O_Player, print_game=True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = O_Player.choose_move(game)
        else:
            square = X_Player.choose_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            letter = 'O' if letter == 'X' else 'X'
        time.sleep(0.8)
    if print_game:
        print('It\'s a tie!')
    
if __name__ == 'main':
    x_Player = AIComputerPlayer('X')
    o_Player = HumanPlayer('O')
    gamePlay = TicTacToe()
    play(gamePlay, x_Player, x_Player, print_game=True)
   