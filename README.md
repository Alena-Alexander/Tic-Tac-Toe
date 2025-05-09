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
        +List[List[String]]game_board
        
        %% Methods
        +make_move(row: int, col: int, symbol: String) Tuple[int, String]
        +is_winner(symbol: String) bool
        +_anti_diag_win(symbol: String) bool
        +_diag_win(symbol: String) bool
        +_col_win(symbol: String) bool
        +_row_win(symbol: String) bool
        +is_full(self) bool
        +get_empty_cells(self) List[Tuple[int, int]]
        +display(self) None
        +__str__(self) String
    }
    
    class Player {
        +String symbol
        
        +__str__() String
        +__dict__() Dict
    }
    
    class HumanPlayer {
        +String symbol
        
        +make_move(board: GameBoard, row: int, col: int) Tuple[bool, String]
    }
    
    class AIPlayer {
        +String symbol
        +MoveStrategy strategy
        
        +find_best_move(board: GameBoard) Tuple[int, int]
    }
    
    class MoveStrategy {
        <<abstract>>
        +find_best_move(board: GameBoard, player: Player)  Tuple[int, int]
    }
    
    class MinimaxStrategy {
        +find_best_move(board: GameBoard, player: Player)  Tuple[int, int]
        +minimax(board: GameBoard, depth: int, is_maximizing_turn: bool, player: Player, opponent: Player) Tuple[int, Union[Player, None]]
    }
    
    class GameController {
        +HumanPlayer human
        +AIPlayer ai
        +GameBoard board
        +HumanPlayer current_player
        
        +switch_player() None
        +check_game_over() Tuple[bool, String]
        +find_best_ai_move()
    }
    
    class TicTacToeGUI {
        +GameController controller
        +Union[QApplication, QApplication] app
        +Union[QGridLayout, QGridLayout]layout
        +List[List[QPushButton, QPushButton]] button_container
        +Union[QLabel, QLabel] label
        
        +setup_ui() None
        +button_click(row: int, col: int, player: Player) None
        +show_result() None
        +reset_gameboard() None
        +run() None
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

# Graph Flowchart of Minimax 

```mermaid
---
title: 1x3 Minimax Board
---

    flowchart TD
        A("Board: [_, _, _,] <br> Turn: X <br> Depth: 0") -->  |X in 0| B("Board: [X, _, _] <br> Turn: O <br> Depth: 1")
        A --> |X in 1| C("Board: [_, X, _] <br> Turn: O <br> Depth: 1")
        A --> |X in 2| D("Board: [_, _, X] <br> Turn: O <br> Depth: 1")
        
        B --> |O in 1| E("Board: [X, O, _] <br> Turn: X <br> Depth: 2")
        B --> |O in 2| F("Board: [X, _, O] <br> Turn: X <br> Depth: 2")
        
        C --> |O in 0| G("Board: [O, X, _] <br> Turn: X <br> Depth: 2")
        C --> |O in 2| H("Board: [_, X, O] <br> Turn: X <br> Depth: 2")
        
        D --> |O in 0| I("Board: [O, _, X] <br> Turn: X <br> Depth: 2")
        D --> |O in 1| J("Board: [_, O, X] <br> Turn: X <br> Depth: 2")
        
        E --> K("Board: [X, O, X] <br>Game over<br> Depth: 3<br>Score: 0<br>(Draw!)")
        
        F --> L("Board: [X, X, O] <br>Game over<br> Depth: 3<br>Score: 10 - 3 = 7<br>(X Wins)")
        
        G --> M("Board: [O, X, X] <br>Game over<br> Depth: 3<br>Score: 10 - 3 = 7<br>(X Wins)")
        
        H --> N("Board: [X, X, O] <br>Game over<br> Depth: 3<br>Score: 10 - 3 = 7<br>(X Wins)")
        
        I --> O("Board: [O, X, X] <br>Game over<br> Depth: 3<br>Score: 10 - 3 = 7<br>(X Wins)")
        
        J --> P("Board: [X, O, X] <br>Game over<br> Depth: 3<br>Score: 0<br>(Draw!)")
        
        K --> Q("Min: 0")
        L --> R("Max: 7")
        M --> S("Max: 7")
        
        N --> T("Max: 7")
        O --> U("Max: 7")
        P --> V("Min: 0")
```

## The 2D Gameboard 
This a layout representation of the 2D Gameboard:

```
  [
    [' ', ' ', ' '],  # Row 0
    [' ', ' ', ' '],  # Row 1
    [' ', ' ', ' ']   # Row 2
  ]
```

This Gameboard is made up of 3 rows with 3 columns contained in each row. Each cell in the Gameboard is\
represented by two indexes [row][col]. Rows cannot be changed but Columns can.

## Here's a visual representation of it

```mermaid
---
title: The 2D Gameboard
---

flowchart TD
    A("Gameboard") --> B("row 0: [' ', ' ', ' ']")
    A --> C("row 1: [' ', ' ', ' ']")
    A --> D("row 2: [' ', ' ', ' ']")
    B --> E("col 0: ' '")
    B --> F("col 1: ' '")
    B --> G("col 2: ' '")
    C --> H("col 0: ' '")
    C --> I("col 1: ' '")
    C --> J("col 2: ' '")
    D --> K("col 0: ' '")
    D --> L("col 1: ' '")
    D --> M("col 2: ' '")
```

## Here's a visual representation of the Flow of the Game

```mermaid
sequenceDiagram
    participant GUI as TicTacToeGUI
    participant Ctrl as GameController
    participant Human as HumanPlayer
    participant AI as AIPlayer
    participant Board as GameBoard
    participant Strat as MinimaxStrategy
    
    GUI-)Human: The Human clicks a button on the GUI
    Board-)Human: A move is made 
    Ctrl-)Board: The Game checks if there's a winner
    Board-)Ctrl: There's no winner yet, nor is there a tie
    Ctrl-)AI: The AI is the current player
    AI-)Strat: The AI finds the best move using minimax
    Strat-)Board: Minmax is evaluated
    Board-)Strat: A best score is determined
    Board-)AI: A move is made by the AI
    GUI-)Board: The Board is updated
    Ctrl-)Board: The Game checks if there's a winner
    Ctrl-)Board: The AI wins
    GUI-)Ctrl: Shows the result of the Game(win, lose, or draw)
    
    
    
    
    

```