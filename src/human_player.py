# File: human_player.py
from typing import overload

from src.game_board import GameBoard
from src.player import Player


class HumanPlayer(Player):
    """
    Represents a human player interacting via GUI clicks.

    Example:
    ========
    >>> from src.human_player import HumanPlayer
    >>> player = HumanPlayer()
    >>> # Note: GameBoard is used as example in this instance and must
    >>> # not be confused for actual game board that is used in the GameController class.
    >>> player.make_move(GameBoard(), 0, 2)

    """

    def __init__(self, symbol: str):
        """
        Initialize the human player.

        Parameters:
            symbol (str): 'X' or 'O'.
        """

        super().__init__(symbol)

    def make_move(self, board: GameBoard, row: int, col: int) -> tuple[bool, str]:
        """
        Attempt to place the player's symbol on the board.

        Parameters:
            board (GameBoard): The game board instance.
            row (int): Row index (0-2).
            col (int): Column index (0-2).

        Returns:
            bool: True if move succeeds, False if invalid.
        """

        return board.make_move(symbol=self.symbol, row=row, col=col)

