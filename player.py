import math, random

class Player():
    """
    A Super class representing a player in a tic-tac-toe game.

    Attributes:
    ----------
    letter : str
        The letter representing the player's move on the board.
    """
    def __init__(self, letter) -> None:
        self.letter = letter

    def choose_move(self, game): 
        pass

class HumanPlayer(Player):
    """
    A class representing a human player in a game of tic-tac-toe.

    Attributes:
    -----------
    letter : str
        The letter representing the player's mark on the board.
    """
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def choose_move(self, game):
        validSquare = False
        val = None
        while not validSquare:
            square = input(self.letter + '\'s turn. Input Move (0-9): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                validSquare = True
            except ValueError:
                print('Invalid Sqaure. Try Again.')
        return val

class ComputerPlayer(Player):
    """
    A class representing a computer player in a Tic Tac Toe game.

    Attributes:
    -----------
    letter : str
        The letter representing the player's mark on the board.
    """
    def __init__(self, letter) -> None:
        super().__init__(letter)

class AIComputerPlayer(Player):
    """
    A class representing an AI computer player in a Tic Tac Toe game.

    Attributes:
    - letter (str): The letter representing the player's mark on the board.
    """
    def __init__(self, letter) -> None:
        super().__init__(letter)