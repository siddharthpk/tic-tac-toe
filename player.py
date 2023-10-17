import math, random

class Player():
    """
    A class representing a player in a tic-tac-toe game.

    Attributes:
    ----------
    letter : str
        The letter representing the player's move on the board.
    """
    def __init__(self, letter) -> None:
        self.letter = letter

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