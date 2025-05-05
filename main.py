# File: main.py
from src.game_board import GameBoard
from src.human_player import HumanPlayer
from src.ai_player import AIPlayer
from src.minimax_strategy import MinimaxStrategy
from src.game_controller import GameController
from src.gui import TicTacToeGUI


def main():
    board = GameBoard()
    human = HumanPlayer("X")
    ai = AIPlayer("O", MinimaxStrategy())
    controller = GameController(human, ai, board)
    gui = TicTacToeGUI(controller)
    gui.run()


if __name__ == "__main__":
    main()
