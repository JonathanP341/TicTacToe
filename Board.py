#Class that updates and prints the board
class Board:
    def __init__(self, rows: list):
        self._rows = rows
        self._winner = "_"

    def __repr__(self):
        for i in range(len(self._rows)): #Will be 3
            print("\n--- --- ---")
            for j in range(len(self._rows[i])): #Will always be 3
                print("|" + self._rows[i][j] + "|", end=" ")
        print("\n--- --- ---")
        return ""

    def changeBoard(self, x: int, y: int, forX: bool, ): # x is the row and y is the column
        if self._rows[y-1][x-1] != "_" or x > 3 or x < 1 or y > 3 or y < 1:
            return False
        else:
            if forX == True:
                self._rows[y-1][x-1] = "X"
            else:
                self._rows[y-1][x-1] = "O"
        return True

    def clearBoard(self):
        self._rows = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    def checkWinner(self):
        #Since its a 3x3 board, there are only a few possible ways to win so we can check for every one of those

        #Checking for across
        win = False
        for i in range(len(self._rows)): #Checking every row
            last = self._rows[i][0] #Setting the first element of every row to the a temp varaible called last which stores the last variable
            for j in range(len(self._rows[i])-1): #Doing it like this because im using len
                if self._rows[i][j + 1] == last: #If they are the same
                    last = self._rows[i][j + 1] #Set last to the now previous element
                    win = True #Setting win to true
                else:
                    win = False #If they arnt equal set it to false
                if win == False: #If they arnt equal then quit because the row
                    break
            if win == True: #If win is set to true after going through the row, then they won
                return last

        #Checking for up down
        win = False #Resetting as the user didnt win
        for i in range(len(self._rows)):
            last = self._rows[0][i]
            for j in range(len(self._rows)-1): #It will always be 2 because we are checking the next two parts of the board
                if self._rows[j+1][i] == last: #If the element in the table is equal to the last one
                    last = self._rows[j+1][i] #Setting last to the the now previous element
                    win = True #Setting win to true
                else:
                    win = False
                if win == False: #If win is set to false break and check the next column
                    break
            if win == True: #If the row is entirely the same element, then you won and return last
                return last

        # Checking for across
        win = False #resetting back to false
        #Since there are only two ways to win diagonally, we can just check manually
        if self._rows[0][0] == self._rows[1][1] == self._rows[2][2] == "X":
            return "X"
        elif self._rows[0][0] == self._rows[1][1] == self._rows[2][2] == "O":
            return "O"

        #Checking the other way
        if self._rows[0][2] == self._rows[1][1] == self._rows[2][0] == "X":
            return "X"
        elif self._rows[0][2] == self._rows[1][1] == self._rows[2][0] == "O":
            return "O"

        return False

    def turn(self, isX: bool):
        print(self)
        if isX == True:
            while True:
                try:
                    xVal = int(input("Enter row: "))
                    yVal = int(input("Enter column: "))
                    break
                except:
                    print("Wrong type, please enter a number")

            correct = self.changeBoard(xVal, yVal, True)
            while correct == False:
                print("Enter a proper part of the board")
                xVal = int(input("Enter row: "))
                yVal = int(input("Enter column: "))
                correct = self.changeBoard(xVal, yVal, True) #add something to change the board here
        elif isX == False:
            while True:
                try:
                    xVal = int(input("Enter row: "))
                    yVal = int(input("Enter column: "))
                    break
                except:
                    print("Wrong type, please enter a number")

            correct = self.changeBoard(xVal, yVal, False)
            while correct == False:
                print("Enter a proper part of the board")
                xVal = int(input("Enter row: "))
                yVal = int(input("Enter column: "))
                correct = self.changeBoard(xVal, yVal, False) #add something to change the board here

        val = self.checkWinner()

        if val == "X":
            print(self)
            return 1
        elif val == "O":
            print(self)
            return 2
        else:
            return 0



'''
b = Board([["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]])
print(b)
b.changeBoard(1, 2, True)
print(b)
b.changeBoard(1, 1, False)
print(b)
b.changeBoard(2, 3, False)
print(b)
winner = b.checkWinner()
if winner == "X":
    print("Player X won!")
elif winner == "O":
    print("Player O won!")
else:
    print("No winner")
'''
