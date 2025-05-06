"""
The Minimax algorithm evaluates all possible moves to find the optimal one.
Here’s the mathematical equation to calculate the best score:

Score Calculation:
If the maximizing player (e.g., X) wins: score = 10 - depth
If the minimizing player (e.g., O) wins: score = -10 + depth
If it’s a draw: score = 0

Depth is the number of moves made so far, used to prioritize quicker wins or slower losses.
Minimax Pseudocode:

minimax(board: Gameboard, depth: int, is_maximizing: bool, player: Player, opponent: Player):
    if maximizing wins:
        return 10 - depth
    if minimizing wins:
        return 10 + depth
    if game is a draw:
        return 0

    # TODO: Going down the game tree
    if is_maximizing:
        best_score: int = -math.inf     # -infinity
        for each empty cell:
            make move for player
            score: int = minimax(board, depth + 1, false, player, opponent)

            # TODO: Going back up the game tree
            undo move
            best_score: int = max(best_score, score)
        return best_score

    # TODO: Going down the game tree
    else:
        best_score: int = math.inf      # +infinity
        for each empty cell:
            make move for opponent
            score: int = minimax(board, depth + 1, true, player, opponent)

            # TODO: Going back up the game tree
            undo move
            best_score: int = min(best_score, score)
        return best_score

The AI chooses the move with the highest score when maximizing (X) or the lowest score when minimizing (O).
"""

# File: minimax_strategy.py
from typing import Union

from src.game_board import GameBoard
from src.move_strategy import MoveStrategy
from src.player import Player
from src.logger import getLogger

log = getLogger(__name__)


class MinimaxStrategy(MoveStrategy):
    """Implements the Minimax algorithm for optimal AI moves."""

    def find_best_move(self, board: GameBoard, player: Player) -> tuple[int, int]:
        """
        Find the optimal move using Minimax.

        Parameters:
            board (GameBoard): The game board instance.
            player (Player): The AI player instance.

        Returns:
            tuple[int, int]: (row, col) of the best move.
        """

        # Assigns best score to the highest negative int
        best_score = float("inf")   # Represents the minimizing player best score

        # Assigns best move to None
        best_move = None
        best_moves = []
        # If player symbol == "X" it changes to "O", else it switches to "X"
        opponent = Player("O" if player.symbol == "X" else "X")


        # Iterates through each row and col in the list of empty cells
        for row, col in board.get_empty_cells():
            # Player makes a move
            board.make_move(row, col, player.symbol)
            # Adds each move the maximizing player makes to the score
            score, winner_player = self.minimax(board, 0, True, player, opponent)


            # Undoes move
            board.game_board[row][col] = ""

            # Choose the best score and returns the best move
            if score < best_score or score == 10:
                # This represents a winning position for the
                # AI Player on the next move, Since (10 - 0)
                # represents a win on the next move for the AI Player.
                # So, this represents an opportunistic player
                if score == 10 and winner_player == player:

                    return row, col
                # And, this represents any other condition to block the
                # human player
                else:
                    best_score = score
                    best_move = row, col
                    best_moves.append(best_move)

        return best_move

    def minimax(self,
                board: GameBoard,
                depth: int,
                is_maximizing_turn: bool,
                player: Player,
                opponent: Player, ) -> tuple[int, Union[Player, None]]:
        """
        Recursively evaluate board states with Minimax.

        Parameters:
            board (GameBoard): Current board state.
            depth (int): Depth in the game tree (moves made).
            is_maximizing_turn (bool): True if maximizing (X), False if minimizing (O).
            player (Player): The AI player (minimizing).
            opponent (Player): The human player (maximizing).

        Returns:
            int: Score of the board state.
        """

        # Checks if the player (maximizing) is a winner returns score
        if board.is_winner(opponent.symbol):
            return 10 + depth, opponent

        # Checks if the opponent (minimizing) is a winner returns score
        if board.is_winner(player.symbol):
            return 10 - depth, player

        # Checks if there are no more moves to be played and if there are no wins
        if board.is_full():
            return 0, None

        if is_maximizing_turn:
            # Assigns best score to the highest negative int
            best_score = -float("inf")
            # Represents the winning player, if any, or None
            winner_player = None
            # Iterates through each cell(tuple) in the list of empty cells
            for cell in board.get_empty_cells():
                # log.info("Maximizing is playing...")
                # Decomposes each cell
                row, col = cell



                # The maximizing player makes a move
                board.make_move(row, col, opponent.symbol)


                # Adds each move the maximizing player makes to the score
                score, winner_player = self.minimax(board, depth + 1, False, player, opponent)


                # Undoes the move made by the player
                board.game_board[row][col] = ""
                log.info(board)

                # Chooses the best score
                best_score = max(best_score, score)



            # Returns the best score
            return best_score, winner_player

        else:
            # Assigns best score to the highest positive int
            best_score = float("inf")
            winner_player = None

            # Iterates through each cell(tuple) in the list of empty cells
            for cell in board.get_empty_cells():

                # log.info("Minimizing is playing...")
                # Decomposes each cell
                row, col = cell


                board.make_move(row, col, player.symbol)

                score, winner_player = self.minimax(board, depth + 1, True, player, opponent)


                # Undoes the move made by the player
                board.game_board[row][col] = ""


                # Chooses the best score
                best_score = min(best_score, score)

            return best_score, winner_player

