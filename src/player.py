# File: player.py
from abc import ABC, abstractmethod
from typing import Annotated

from src.game_board import GameBoard


class Player(ABC):
    """
    Parent base class for players in the game.

    Example:
    ========
    >>> from src.player import Player

    >>> class AIPlayer(Player):

    >>> class HumanPlayer(Player):
    """

    symbol: Annotated[str, "Player symbol: 'X' or 'O'"]

    def __init__(self, symbol: str):
        """
        Initialize a player with a symbol.

        Parameters:
            symbol (str): 'X' or 'O'.
        """
        self.symbol = symbol

    def __str__(self):
        """
        Returns a dictionary key: value converted to a string.

        :return: (str): A symbol key value pair.
        """
        return str(self.__dict__())

    def __dict__(self):
        return {"Symbol": self.symbol}
