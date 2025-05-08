"""
1. Button is clicked
2. Human player makes move on the board class(human_player.make_move)
3. Human players make a move on GUI representing the board
4. Symbol is placed on the Label on the button on the board
5. Players are switched
6. AI player switched(game_controller.switch_players)
7. AI player finds best move using the game_controller using the find_best_ai_move function
8. AI player makes move in Gameboard class
9. Adds to Label of the button
10. Check if the game is over
11. Displays message based on who won
12. Switch player again and the human player has to click a button
13. The game repeats until a winner is found or it's a draw
"""
import datetime

# File: gui.py
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QActionEvent, QAction, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, \
    QWidget, QGridLayout, QWidgetAction
from functools import partial
# Needed to access list of command line arguments
import sys
from src.game_controller import GameController
from src.human_player import HumanPlayer
from src.ai_player import AIPlayer
from src.minimax_strategy import MinimaxStrategy
from src.game_board import GameBoard
from src.logger import getLogger
from src.player import Player
from dataclasses import dataclass

log = getLogger(__name__)


# Subclass QMainWindow to customize the main window
class TicTacToeGUI(QMainWindow):
    """PyQt6-based GUI for Tic-Tac-Toe."""
    # Creates an instance of the app, with command line arguments
    app = QApplication(sys.argv)

    def __init__(self, controller: GameController):
        """
        Initialize the GUI with a controller.

        Parameters:
            controller (GameController): The game controller instance.
        """

        super().__init__()
        self.controller = controller

        # Change title of the main window
        self.setWindowTitle("Tic-Tac-Toe")

        # The Fixed size of the window
        self.setFixedSize(285, 350)

        # Creates a 3x3 grid and Allows you to place widgets in the form of a grid
        self.layout = QGridLayout()

        # Create a container for the buttons
        self.button_container = [[QPushButton("", self) for _ in range(3)] for _ in range(3)]
        self.label = QLabel()

    def setup_ui(self) -> None:
        """
        Create the 3x3 button grid and status label.

        Returns:
            Returns None
        """
        # Set a button for each cell (r, c) on the gui game board
        for r in range(3):
            for c in range(3):
                # Get the buttons from the container
                button: QPushButton = self.button_container[r][c]

                # Sets a fixed size for each button
                button.setFixedSize(80, 75)

                # Set the button font
                button.setFont(QFont('Times', 48))

                # Add an event action to the button
                button.clicked.connect(partial(self.button_click, r, c, self.controller.current_player))

                # Add the button to the grid layout
                self.layout.addWidget(button, r, c)

                # Set the grid layout alignment
                self.layout.setAlignment(button, Qt.AlignmentFlag.AlignHCenter)

                # Add button to button container
                self.button_container[r][c] = button

        # Set the fixed size for the Label
        self.label.setText("")
        self.label.setWordWrap(True)

        # Add Label to the grid layout
        self.layout.addWidget(self.label, 4, 0, 2, 3)

        # Create and exit button
        reset_button = QPushButton("Reset Game", self)

        # Set the exit button font
        reset_button.setFont(QFont('Times', 10))

        # Set the fixed size for the button
        reset_button.setFixedSize(80, 50)

        # Set button click event action
        reset_button.clicked.connect(partial(self.reset_gameboard))

        # Add the button to the grid layout
        self.layout.addWidget(reset_button, 3, 0)

        # Create and exit button
        exit_button = QPushButton("Exit Game", self)

        # Set the exit button font
        exit_button.setFont(QFont('Times', 10))

        # Set the fixed size for the button
        exit_button.setFixedSize(80, 50)

        # Add event action to exit button
        exit_button.clicked.connect(partial(exit, 0))

        # Add the button to the grid layout
        self.layout.addWidget(exit_button, 3, 2)

        # Creates an instance of the QWidget class,
        # which is also a widget used as container for other
        # widgets(layout)
        widget = QWidget()

        # Applies a layout widget to a widget
        widget.setLayout(self.layout)

        # Applies widget to the center of the window
        self.setCentralWidget(widget)

    def button_click(self, row: int, col: int, player: Player) -> None:
        """
        Handle button clicks for human moves.

        Parameters:
            :param row: Row index (0-2).
            :param col: Column index (0-2)
            :param player: The current player.
        """
        log.info(f"Player: {player.symbol}, clicks at: ({row}, {col})")

        # TODO: step 1:
        #   Check if button cell is not empty on the gui and the
        #   game board, and display a message
        #   to try another button cell or just try again
        #   and return None to stop executing the below code.
        #   Remember that the gui game board buttons are found in the `self.button_container`.

        # Retrieves a button from the button container
        button: QPushButton = self.button_container[row][col]

        # If button cell on GUI or game board != "" display a message the says "Try again!"
        if button.text() != "" and self.controller.board.game_board[row][col] != "":
            self.label.setText("Try again!")

            # Return None
            return None

        # TODO: step 2:
        #   If the button cell is empty, then place the player symbol
        #   at that (r, c) for the cell and update the game board

        # If button cell on GUI or game board == "" the player makes a move on the
        # GUI board and the game board, and the board is updated
        if button.text() == "" and self.controller.board.game_board[row][col] == "":
            self.controller.board.make_move(row, col, player.symbol)
            button.setText(player.symbol)
            self.show()

        # TODO: step 3:
        #   Check if the last move made was a winning move;
        #   If it is a winning move then display the message on the label and
        #   return None to stop executing the code that follows below.
        #   Else continue to switch to the AI player.

        # Passes the tuple containing a boolean and a string to the variables
        # is_over, result_message
        is_over, result_message = self.controller.check_game_over()

        # If the AI or the player wins, or it was a draw return a message displaying
        # the result message of who won, else it switches to the AI player
        if is_over:
            self.label.setText(result_message)

            return None
        else:
            self.controller.switch_player()
            player = self.controller.current_player

        # TODO: step 4:
        #   Find the best move for the AI player using the
        #   game controller class and make a move on both the
        #   game board and gui game board

        # Get the row and col of the best move
        row, col = self.controller.find_best_ai_move()

        # Retrieves a button from the button container
        button: QPushButton = self.button_container[row][col]

        # If button cell on GUI or game board != "" display a message the says "Try again!"
        if button.text() != "" and self.controller.board.game_board[row][col] != "":
            self.label.setText("Try again!")

            # Return None
            return None

        # If button cell on GUI or game board == "" the player makes a move on the
        # GUI board and the game board, and the board is updated
        if button.text() == "" and self.controller.board.game_board[row][col] == "":
            self.controller.board.make_move(row, col, player.symbol)
            button.setText(player.symbol)
            self.show()

            # TODO: step 5:
            #   Check if the last move made was a winning move;
            #   If it is a winning move then display the message and
            #   return None to stop executing the code that follows below.
            #   Else continue to switch to the Human player and return None,
            #   So that the user can pick another cell.

            # Passes the tuple containing a boolean and a string to the variables
            # is_over, result_message
            is_over, result_message = self.controller.check_game_over()

            # If the AI or the player wins, or it was a draw return a message displaying
            # the result message of who won, else it switches to the AI player
            if is_over:
                self.label.setText(result_message)

                # We switch turn back to human player. So the user can start a new game.
                self.controller.switch_player()
                return None
            else:
                self.controller.switch_player()

    def show_result(self) -> None:
        """
        Display the game result.
        """
        is_over, result_message = self.controller.check_game_over()

        if is_over == True:
            self.label.setText(result_message)
            return None

    def reset_gameboard(self):
        # Kill two birds with one stone!
        for r in range(3):
            for c in range(3):
                # Resets the gui game board
                button: QPushButton = self.button_container[r][c]
                button.setText("")
                # Resets the game board in the GameBoard class
                self.controller.board.game_board[r][c] = ""

    def run(self) -> None:
        """Start the GUI application."""
        # Creates the 3x3 grid
        self.setup_ui()

        # Shows the window
        self.show()

        # Starts an event loop
        sys.exit(self.app.exec())


#################################################
@dataclass
class Person:
    """
    Some example class.

    Attributes:
        name (str): person's name
        age (int): person's age
        dob (date): person's dob
    """
    name: str
    age: int
    dob: datetime.date


#################################################


if __name__ == "__main__":
    person = Person("John", 25, datetime.date.fromisoformat("2025-01-03"))
    print(person)


