# The Tic-Tac-Toe Minmax Algorithm

Is where a human player competes in a game of Tic-Tac-Toe against an AI\
that uses the Minmax Algorithm, which is a strategy where after the first\
move is made by the human player and AI search through every possible it\
could make and chooses the best possible move. During the minmax Strategy the human\
player is known as the maximizing player, and the AI is referred to as the\
minimizing player. The score for the game is determined by the total of moves made\
(known as the depth) by both players before there's a win, loss, or draw.\

The minmax algorithm is made of classes that represents every aspect of the game\
of Tic-Tac-Toe, for the Gameboard includes function that checks if a player has won\
based on where they place there symbol on the board and checks if the cells on the\
are full.

This algorithm includes classes that inherit certain class data attributes and\
function from another class.

## The Player class
The player class represents the parent base class for\
the human player class and AI class, enabling them to\
inherit the symbol('X' or 'O') from it.

## The AI player class
The AI class represents the AI that plays against the human\
it includes the find best move function which is a function\
that uses the minmax strategy to search for the best possible\
move to make, and returns a tuple containing two ints.

## The Human Player class
The Human player class represents the human player that plays\
against the AI it includes the make move function that plays a\
symbol onto the board independently by calling the make move function\
from the Game board class, and returns a tuple containing bool and a str.

## The Gameboard class 
The Gameboard class represents a 3 by 3 2D board that the Human\
player will be playing against the AI on. It includes the make move\
function which places a symbol on the board. The is winner class,\
calls four other functions in which based on the positions symbols\
are placed on the board three in a row, col, diagonal, or anti-diagonal\
it returns True else the function would return False.

There's also the is full function checks if the Game board it includes a\
conditional statement that says if there are 0 empty cell in the board\
return True else return False.

The Game board also includes a couple of other functions, the get empty\
cells function which basically stores the cells without symbols within them\
into an empty list and returns list containing tuples with two int.

The display function which prints the board that the Human\
player will be playing against the AI on.

It includes the make_move function which places a symbol on the board.

The is_winner function calls four other functions in which based on the positions symbols\
are placed on the board three in a row, col, diagonal, or anti-diagonal\
it returns True if there was a winner else the function would return False.

There's also the is full function checks if the Game board it includes a\
conditional statement that says if there are 0 empty cell in the board\
return True else return False.

A built-in __str__ function that also prints a sketch of the board.

## The Move Strategy class
The move strategy class which is an abstract class for the AI players\
move strategy.

## The Game Controller
The Game controller class controls the flow of the game, it includes 3\
functions. The switch_player switches the current player between the Human\
player and AI player. The check_game_over function returns a tuple\
containing a bool and a str based on whether there's a winner or the game\
board is full.

## The Minimax Strategy class
The minimax function is a strategy is a used by the AI so that it's able to go through\
every possible move to make in a game and choose the most optimal move. And\
depending on the depth which is the amount of moves made by each player the\
score will be determined. The Human players identifies as the maximizing\
player and the AI the minimizing player, and the role of the AI player is to\
minimize the maximizing players chance of winning by going through multiple\
states of the game board until it finds the best optimal move.

The find_best_move function which return a tuple containing to integers aka the best\
score for the AI if it results in a win.

## The GUI
The GUI is a 3 by 3 Graphical Grid that actually represents the Gameboard it\
includes buttons that when pressed a symbol is added to them and a reset button\
to reset the Gameboard whenever, and an exit button to terminate the board.

```mermaid
---
Tic-Tac-Toe Minimax Algorithm
---
classDiagram
    class GameBoard {
        %% Attributes
        +self
        
        %% Methods
        +__init__(self)
        +make_move(row, col, symbol) Tuple[int, str]
        +is_winner(symbol) bool
        +_anti_diag_win(symbol) bool
        +_diag_win(symbol) bool
        +_col_win(symbol) bool
        +_row_win(symbol) bool
        +is_full(self) bool
        +get_empty_cells(self) List[Tuple[int, int]]
        +display(self) None
        +__str__(self) str
    }
    
    class Player {
        
    }
    class HumanPlayer {
        
    }
    class AIPlayer {
        
    }
    class MoveStrategy {
        <<abstract>>
    }
    class MinimaxStrategy {
        
    }
    class GameController {
        
    }
    class TicTacToeGUI {
        
    }
    
    note for Gameboard "Manages the 3x3 board state"
    note for Player "Base class for players"
    note for HumanPlayer "Represents the human player"
    note for AIPlayer "Represent the AI player"
    note for MoveStrategy "Defines move logic of the Game"
    note for MinimaxStrategy "Represents the minmax Algorithm for the AI"
    note for GameController "Controls the flow of the Game"
    note for TicTacToeGUI "Creates a GUI of the GameBoard"
    
    %% Inheritance
    Player <|-- HumanPlayer
    Player <|-- AIPlayer
    MoveStrategy <|-- MinimaxStrategy
    
    %% Aggregation: Classes that are assembled together
    %% to create a more complex object
    AIPlayer o--> MoveStrategy
    GameController o--> HumanPlayer
    GameController o--> AIPlayer
    GameController o--> GameBoard
    TicTacToeGUI o--> GameController
```
