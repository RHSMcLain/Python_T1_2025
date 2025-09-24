# To make a function: we use 'def _functionname():'
def drawSquare():
    squareSize = 5
    lpRows = 0
    while lpRows < squareSize:
        lpRows += 1
        lpLine = 0
        while lpLine < squareSize:
            lpLine += 1
            print("*", end="")
        print()

n = 0
while n < 10:
    n += 1
    drawSquare() #we call the function with its name and parentheses
    print()


