# Project Name: Super Tic-Tac-Toe

Code by: Gameboy612<br>
Inspired by: https://www.youtube.com/shorts/_Na3a1ZrX7c



Description:
This is a recreation of the game, Super Tic-Tac-Toe.<br>
(Also known as Ultimate Tic-Tac-Toe)

This program uses an OOP approach to recreate the game in Python.

Each smaller board is defined as a class (SmallGame())
And the entire board is defined as another class (FullGame())

9 SmallGame objects are stored as pointers in the FullGame object,
which can then be used to control the entire board.



## `Tiles()`

Description:
    
    This class is used to save unicode characters.
    Objects are not supposed to be created with this class.



Attributes: (6)
1. `X`

    The cross unicode character.

2. `O`

    The circle unicode character.

3. `Blank`

    The filler unicode character for empty spaces.

4. `HighlightedBlank`

    The filler unicode character for highlighted inner-games with empty spaces.

5. `Wall`

    The unicode character used to draw the large grid.

6. `RedSquare`

    The unicode character used to draw the large O and large X.



Methods:
1. `getTile(x: (True | False | None), highlight: bool) => char`

    This method accepts a slot, and returns the required tile for it.

    This method is not designed for calling as an object,<br>but called using Tiles.getTile(x, highlight).


## `SmallGame()`
Description:

    This class is used to store each individual inner-game.



Attributes: (2)
1. `self.winner (None | -1 | True | False)`

        None:   Inner-game is still active
        -1:     Ended in a draw
        True:   O won
        False:  X won

2. `self.grid (True | False | None)[9]`

        True:   O
        False:  X
        None:   Empty Square



Methods:
1. `checkWin() => (True | False)`

      This is used to check whether a winning condition is met in a cell.

2. `registerSquare(turn: bool, slot: int) => (False | None)`

    This attempts to set the grid's slot to the current turn.

    If the slot is empty, then this returns False, and the move would not be made.
    Otherwise, the program will set the slot to the current turn.

    After the slot is set, self.checkWin() is ran, to check whether a winning condition is met.
    If met, self.winner is set to the current turn (True | False), effectively ending the inner-game.
          
    Finally, the program checks whether None exists in self.grid.
    If not exist, then self.winner is set to draw state (-1).

3. `showgrid(highlight: bool) => ("")[3]`

    If self.winner is either True, False or -1, a preset is returned for Big O, Big X and Draw respectively.

    Otherwise, a custom output is returned, where the smaller grid is divided into a 3x3 char list 
    (or a length 3 string in a length 3 list)

## `FullGame()`
Description:

    This class is used to store the whole game.



Attributes: (2)
1. `self.turn (True | False)`

        True:   O's turn
        False:  X's turn

2. `self.grids (SmallGame())[9]`

    Elements are SmallGame() objects.



Methods:
1. `checkWin() => (True | False)`

    This is used to check whether a winning condition is met in the whole game.

2. `isAvailable(gridnum: int, slotnum: int) => (True | False)`

    Returns whether the slot chosen is available.

3. `assignGrid(gridnum: int, slotnum: int, turn: bool)`

    This forwards the assigning request to the registerSquare() method from SmallGame() object.
    
4. `showgrid(highlightnum: int [= -1])`

    Prints out the game's current state.

5. `getUser() => ("O" | "X")`

    Returns the current turn in string form.
        
        True:   "O"
        False:  "X"
6. `start() => (True | False | None)`
    
    Starts the game.