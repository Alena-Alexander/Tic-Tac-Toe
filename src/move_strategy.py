# File: move_strategy.py
from abc import ABC, abstractmethod
from src.game_board import GameBoard
from src.player import Player


class MoveStrategy(ABC):
    """Abstract base class for AI move strategies (Strategy Pattern)."""
    @abstractmethod
    def find_best_move(self, board: GameBoard, player: Player) -> tuple[int, int]:
        """
        Determine the best move for the player.

        Parameters:
            board (GameBoard): The game board instance.
            player (Player): The AI player instance.

        Returns:
            tuple[int, int]: (row, col) of the best move.
        """
        pass
