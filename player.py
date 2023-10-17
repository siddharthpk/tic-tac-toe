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
    
    def choose_move(self, game):
        square = random.choice(game.available_moves())
        return square

class AIComputerPlayer(Player):
    """
    A class representing an AI computer player in a Tic Tac Toe game.

    Attributes:
    - letter (str): The letter representing the player's mark on the board.
    """
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def choose_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game,self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_Player = self.letter
        min_Player = '0' if player == 'X' else 'X'
        utility_Fn = [0,1,-1]

        if state.current_winner == min_Player:
            return {
                'position' : None,
                'score':utility_Fn[1]*(state.num_empty_squares()+ 1) if min_Player == max_Player 
                        else utility_Fn[-1]*(state.num_empty_squares() + 1)
            }
        elif not state.empty_squares():
            return {
                'position' : None,
               
                'score': utility_Fn[0]
            }
        
        if player == max_Player:
            best = {
                'position': None,
                'score': -math.inf
            }
        else:
            best = {
                'position': None,
                'score': math.inf
            }

        for possible_move in state.available_moves():
            # Making a simulated move
            state.make_move(possible_move, player)
            simulated_score = self.minimax(state, min_Player)

            # Undoing move
            state.board[possible_move] = ' '
            state.current_winner = None
            simulated_score['position'] = possible_move

            if player == max_Player:
                if simulated_score['score'] > best['score']:
                    best = simulated_score
            else:
                if simulated_score['score'] < best['score']:
                    best = simulated_score
        return best

