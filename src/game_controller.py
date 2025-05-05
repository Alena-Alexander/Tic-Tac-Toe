# File: game_controller.py
from src.ai_player import AIPlayer
from src.game_board import GameBoard
from src.human_player import HumanPlayer
from src.logger import getLogger

log = getLogger(__name__)


class GameController:
    """
    Controls game flow, alternating between players.

    Example:
    ========
    >>> # If the AI or the player wins, or it was a draw return a message displaying
    >>># the result message of who won, else it switches to the AI player
    >>> if is_over:
    >>>     self.label.setText(result_message)
    >>>     log.info("The Human player wins!")
    >>>     return None
    >>> else:
    >>>     self.controller.switch_player()
    >>>     player = self.controller.current_player
    >>>     log.info(f"Its the {player} turn!")
    """

    def __init__(self, human: HumanPlayer, ai: AIPlayer, board: GameBoard):
        """
        Initialize the game with players and a board.

        Parameters:
            human (HumanPlayer): The human player.
            AI (AIPlayer): The AI player.
            board (GameBoard): The game board instance.
        """

        self.human = human
        self.ai = ai
        self.board = board
        self.current_player = human

    def switch_player(self) -> None:
        """
        Switch the current player between human and AI.

        Returns:
        ========
        Returns None
        """

        if self.current_player == self.human:
            self.current_player = self.ai
        else:
            self.current_player = self.human

    def check_game_over(self) -> tuple[bool, str]:
        """
        Check if the game has ended.

        Returns:
            tuple[bool, str]: (is_over, result_message).
        """

        # Checks if the human player is a winner
        # return a tuple including a bool and result
        # message
        if self.board.is_winner(self.human.symbol):
            # return a tuple including a bool and result
            # message
            return True, "The Human wins"

        # Checks if the AI player is a winner
        if self.board.is_winner(self.ai.symbol):
            # return a tuple including a bool and result
            # message
            return True, "The AI wins"

        # Checks if there are no more moves to be played and if there are no wins
        if self.board.is_full():
            # return a tuple including a bool and result
            # message
            return True, "It's a draw!"
        else:
            return False, ""

    def find_best_ai_move(self):
        """
        Returns the best AI move.

        Returns:
        ========
        tuple[int, int]: The best move
        """
        return self.ai.find_best_move(self.board)
