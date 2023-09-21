# ---------------------------------------------------------------
# Project Name: Super Tic-Tac-Toe
#
# Code by: Gameboy612
# Inspired by: https://www.youtube.com/shorts/_Na3a1ZrX7c
#
#
#
# Description:
# This is a recreation of the game, Super Tic-Tac-Toe.
# (Also known as Ultimate Tic-Tac-Toe)
#
# This program uses an OOP approach to recreate the game in Python.
#
# Each smaller board is defined as a class (SmallGame())
# And the entire board is defined as another class (FullGame())
#
# 9 SmallGame objects are stored as pointers in the FullGame object,
# which can then be used to control the entire board.
#
# ---------------------------------------------------------------



# ---------------------------------------------------------------
#  _________________________________________________
# |                                                 |
# |                                                 |
# | Tiles()                                         |
# |                                                 |
# |_________________________________________________|
#
# Description:
#       This class is used to save unicode characters.
#       Objects are not supposed to be created with this class.
#
#
#
# Attributes: (6)
# 1. X
#       The cross unicode character.
#
# 2. O
#       The O unicode character.
#
# 3. Blank
#       The filler unicode character for empty spaces.
#
# 4. HighlightedBlank
#       The filler unicode character for highlighted inner-games with empty spaces.
#
# 5. Wall
#       The unicode character used to draw the large grid.
#
# 6. RedSquare
#       The unicode character used to draw the large O and large X.
#
#
#
# Methods:
# 1. getTile(x: (True | False| None), highlight: bool) => char
#       This method accepts a slot, and returns the required tile for it.
#       This method is not designed for calling as an object,
#       but called using Tiles.getTile(x, highlight).
# ---------------------------------------------------------------
class Tiles:
    X = "❌"
    O = "⭕"
    Blank = "⬜"
    HighlightedBlank = "🔲"
    Wall = "⬛"
    RedSquare = "🟥"

    def getTile(x, highlight):
        if x == True:
            return Tiles.O
        if x == False:
            return Tiles.X
        if x == None:
            if highlight:
                return Tiles.HighlightedBlank
            return Tiles.Blank
        return Tiles.Wall


# ---------------------------------------------------------------
#  _________________________________________________
# |                                                 |
# |                                                 |
# | SmallGame()                                     |
# |                                                 |
# |_________________________________________________|
#
# Description:
#       This class is used to store each individual inner-game.
#
#
#
# Attributes: (2)
# 1. self.winner (None | -1 | True | False)
#       None:   Inner-game is still active
#       -1:     Ended in a draw
#       True:   O won
#       False:  X won
#
# 2. self.grid (True | False | None)[9]
#       True:   O
#       False:  X
#       None:   Empty Square
#
#
#
# Methods:
# 1. checkWin() => (True | False)
#       This is used to check whether a winning condition is met in a cell.
#
# 2. registerSquare(turn: bool, slot: int) => (False | None)
#       This attempts to set the grid's slot to the current turn.
#       If the slot is empty, then this returns False, and the move would not be made.
#       Otherwise, the program will set the slot to the current turn.
#
#       After the slot is set, self.checkWin() is ran, to check whether a winning condition is met.
#       If met, self.winner is set to the current turn (True | False), effectively ending the inner-game.
#       
#       Finally, the program checks whether None exists in self.grid.
#       If not exist, then self.winner is set to draw state (-1).
#
# 3. showgrid(highlight: bool) => ("")[3]
#       If self.winner is either True, False or -1, a preset is returned for Big O, Big X and Draw respectively.
#       Otherwise, a custom output is returned, where the smaller grid is divided into a 3x3 char list 
#       (or a length 3 string in a length 3 list)
# ---------------------------------------------------------------
class SmallGame:
    winner = None

    def __init__(self):
        self.grid = [None for i in range(9)]

    def checkWin(self):
        grid = self.grid
        return ((grid[0] == grid[1] == grid[2] != None) or 
                (grid[3] == grid[4] == grid[5] != None) or 
                (grid[6] == grid[7] == grid[8] != None) or 
                (grid[0] == grid[3] == grid[6] != None) or 
                (grid[1] == grid[4] == grid[7] != None) or 
                (grid[2] == grid[5] == grid[8] != None) or 
                (grid[0] == grid[4] == grid[8] != None) or 
                (grid[2] == grid[4] == grid[6] != None))


    def registerSquare(self, turn, slot):
        if self.grid[slot] != None:
            return False
        self.grid[slot] = turn
        
        if self.checkWin():
            self.winner = turn
        
        elif None not in self.grid:
            self.winner = -1
    
    def showgrid(self, highlight):
        if self.winner != None:
            # O Case
            if self.winner == True:
                return [
                    Tiles.RedSquare + Tiles.RedSquare   + Tiles.RedSquare,
                    Tiles.RedSquare + Tiles.Blank       + Tiles.RedSquare,
                    Tiles.RedSquare + Tiles.RedSquare   + Tiles.RedSquare,
                    ]
            # Draw Case
            elif self.winner == -1:
                return [
                    Tiles.Wall      + Tiles.Wall        + Tiles.Wall,
                    Tiles.Wall      + Tiles.Wall        + Tiles.Wall,
                    Tiles.Wall      + Tiles.Wall        + Tiles.Wall,
                    ]
            # X Case
            return [
                    Tiles.RedSquare + Tiles.Blank       + Tiles.RedSquare,
                    Tiles.Blank     + Tiles.RedSquare   + Tiles.Blank,
                    Tiles.RedSquare + Tiles.Blank       + Tiles.RedSquare,
                ]
        
        output = ["", "", ""]
        for i in range(0, 9):
            output[i // 3] += Tiles.getTile(self.grid[i], highlight)
        return output

        
# ---------------------------------------------------------------
#  _________________________________________________
# |                                                 |
# |                                                 |
# | FullGame()                                      |
# |                                                 |
# |_________________________________________________|
# 
# Description:
#       This class is used to store the whole game.
#
#
#
# Attributes: (2)
# 1. self.turn (True | False)
#       True:   O's turn
#       False:  X's turn
#
# 2. self.grids (SmallGame())[9]
#       Elements are SmallGame() objects.
#
#
#
# Methods:
# 1. checkWin() => (True | False)
#       This is used to check whether a winning condition is met in the whole game.
#
# 2. isAvailable(gridnum: int, slotnum: int) => (True | False)
#       Returns whether the slot chosen is available.
#
# 3. assignGrid(gridnum: int, slotnum: int, turn: bool)
#       This forwards the assigning request to the registerSquare() method from SmallGame() object.
# 
# 4. showgrid(highlightnum: int [= -1])
#       Prints out the game's current state.
#
# 5. getUser() => ("O" | "X")
#       Returns the current turn in string form.
#       True:   "O"
#       False:  "X"
# 6. start() => (True | False | None)
#       Starts the game.
# ---------------------------------------------------------------
class FullGame:
    turn = True
    def __init__(self):
        self.grids = [SmallGame() for i in range(9)]

    def checkWin(self):
        grid = [self.grids[i].winner for i in range(9)]
        return ((grid[0] == grid[1] == grid[2] != None) or
                (grid[3] == grid[4] == grid[5] != None) or
                (grid[6] == grid[7] == grid[8] != None) or
                (grid[0] == grid[3] == grid[6] != None) or
                (grid[1] == grid[4] == grid[7] != None) or
                (grid[2] == grid[5] == grid[8] != None) or
                (grid[0] == grid[4] == grid[8] != None) or
                (grid[2] == grid[4] == grid[6] != None))


    def isAvailable(self, gridnum, slotnum):
        if self.grids[gridnum].winner != None:
            return False

        return self.grids[gridnum].grid[slotnum] == None

    def assignGrid(self, gridnum, slotnum, turn):
        self.grids[gridnum].registerSquare(turn, slotnum)

    def showgrid(self, highlightnum=-1):
        lines = ["" for i in range(9)]
        for i in range(15):
            print()

        for i in range(0, 9):
            output = self.grids[i].showgrid(i == highlightnum)
            for j in range(3):
                lines[i // 3 * 3 + j] += output[j]
                if (i % 3 != 2):
                    lines[i // 3 * 3 + j] += Tiles.Wall
        
        for i in range(9):
            print(lines[i])
            if i % 3 == 2 and i != 8:
                print("".join([Tiles.Wall for i in range(11)]))

    def getUser(self):
        if self.turn:
            return "O"
        return "X"

    def start(self):
        # ask_for_grid(init: bool) => int range([0, 8])
        #       Asks user which grid to start in?
        #       init parameter toggles whether the program adds the user into the question.
        def ask_for_grid(init=False):
            chosengrid = -1

            while not ((1 <= chosengrid <= 9) and self.grids[chosengrid - 1].winner == None):
                if init:
                    chosengrid = input("Which grid do u want to start in?\n")
                else:
                    chosengrid = input(f"{self.getUser()}! Which grid do u want to start in?\n")
                try:
                    chosengrid = int(chosengrid)
                except ValueError:
                    chosengrid = -1
            return chosengrid - 1


        # Initializes the grid position
        chosengrid = ask_for_grid(True)

        # Game Loop
        while 1:
            self.showgrid(chosengrid)

            # Collect user input here
            chosenslot = -1

            while not (1 <= chosenslot <= 9):
                chosenslot = input(f"{self.getUser()}! Which slot do u want to choose?\n")
                try:
                    chosenslot = int(chosenslot)
                except ValueError:
                    chosenslot = -1
            chosenslot -= 1


            # Checks availability, if available assign move. Else, print error and continue looping.
            if self.isAvailable(chosengrid, chosenslot):
                self.assignGrid(chosengrid, chosenslot, self.turn)
                
                # Checks win condition for large board. If won, return to end the game.
                if self.checkWin():
                    self.showgrid()
                    return self.turn
                
                # Check for whether all boards have finished their games.
                # Count Trues and Falses to find who has more total slots.
                # Returns respective values depending on condition.
                elif None not in [x := self.grids[i].winner for i in range(9)]:
                    # when draw
                    countT = 0
                    countF = 0
                    for a in x:
                        if a == True:
                            countT += 1
                        elif a == False:
                            countF += 1
                    if countT > countF:
                        return True
                    elif countF > countT:
                        return False
                    else:
                        return None
                
                # Set the next turn's grid to the current chosen slot.
                chosengrid = chosenslot

                # Sends the turn to the next player.
                self.turn = not self.turn

                # Checks if the next turn's grid is a finished game.
                # If it is, then allow the user to pick any game to continue in.
                if self.grids[chosengrid].winner != None:
                    self.showgrid()
                    chosengrid = ask_for_grid()
            else:
                print("Slot not available!")






# Declare the Game Object
game = FullGame()
winner = game.start()

# After game.start(), either True, False or None is returned, which is checked and shown.
if winner == True:
    print("O won!")
elif winner == False:
    print("X won!")
else:
    print("Draw")