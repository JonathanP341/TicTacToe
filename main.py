# This is a useless/gutter class
# My version of Tic Tac Toe will have 3 things:
    # X, O and _ where _ is nothing and X and O are both other things
from Board import Board

b = Board([["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]])

#Running the game
keepPlaying = True
while keepPlaying == True: #While the user wants to keep playing
    isX = False #Setting isX to false because the beginning of the
    b.clearBoard() # Have a method to clear the board
    for i in range(9):
        if isX == True:
            isX = False
            print("\nPlayer O Turn")
        elif isX == False:
            isX = True
            print("\nPlayer X Turn")
        val = b.turn(isX)

        if val == 1:
            print("Player X Won!! ")
            break
        elif val == 2:
            print("Player O Won!!")
            break
        elif val == 0:
            pass
    print(b) #Printing the board after winning or finishing

    userInput = input("\n\nWould you like to keep playing?(Y/N): ")
    if userInput.upper() == "Y":
        keepPlaying = True
    else:
        keepPlaying = False
