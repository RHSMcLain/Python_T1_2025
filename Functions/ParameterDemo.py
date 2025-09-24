# To request needed information, we add a parameter between the parentheses
def drawSquare(squareSize):    
    lpRows = 0
    while lpRows < squareSize:
        lpRows += 1
        lpLine = 0
        while lpLine < squareSize:
            lpLine += 1
            print("*", end="")
        print()
# We can also take in multiple values
def drawRectangle(height, width):    
    lpRows = 0
    while lpRows < height:
        lpRows += 1
        lpLine = 0
        while lpLine < width:
            lpLine += 1
            print("*", end="")
        print()
drawRectangle(3,5) #draws a rectangle that is 3 hight by 5 wide
print()
drawRectangle(12,10)
drawSquare(30)
print("-----------------------")
n = 0
while n < 10:
    n += 1
    drawSquare(n) #to send it the needed value, we put the value in the parentheses when we call it

    print()