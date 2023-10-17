class TicTacToe():
    #Constructor to initialize the board and the current winner
    def __init__(self) -> None:
        self.board  = self.make_board()
        self.current_winner = None
    
    #Returns the  board 
    @staticmethod
    def make_board():
        return [ ' ' for _ in range(9)]