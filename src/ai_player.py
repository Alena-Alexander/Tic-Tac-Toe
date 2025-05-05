# File: ai_player.py
from typing import overload

from src.game_board import GameBoard
from src.player import Player
from src.move_strategy import MoveStrategy


class AIPlayer(Player):
    """
    Represents an AI player using a strategy for moves.

    Example
    =======
    >>> if button.text() == "" and self.controller.board.game_board[row][col] == "":
    >>>     self.controller.board.make_move(row, col, player.symbol)
    """

    def __init__(self, symbol: str, strategy: MoveStrategy):
        """
        Initialize the AI with a symbol and strategy.

        Parameters:
            symbol (str): 'X' or 'O'.
            strategy (MoveStrategy): The move-making strategy.
        """

        super().__init__(symbol)
        self.strategy = strategy

    def find_best_move(self, board: GameBoard) -> tuple[int, int]:
        """
        Use the strategy to pick and make a move.

        Parameters:
            board (GameBoard): The game board instance.

        Returns:
            tuple[int, int]: (row, col) of the chosen move.
        """

        return self.strategy.find_best_move(board, self)
