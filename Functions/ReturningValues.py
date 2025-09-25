#
# With the return statement we can send a value back to the place that called it
#
def drawSquare(squareSize, symbol = "#"):    #takes a single parameter, plus an optional 'symbol' value that defaults to '#'
    lpRows = 0
    while lpRows < squareSize:
        lpRows += 1
        lpLine = 0
        while lpLine < squareSize:
            lpLine += 1
            print(symbol, end="")
        print()
# We will have draw rectangle calculate the area of our rectangle and send it back
def drawRectangle(height, width):    #takes two values
    lpRows = 0
    while lpRows < height:
        lpRows += 1
        lpLine = 0
        while lpLine < width:
            lpLine += 1
            print("*", end="")
        print()
    return height * width # halts execution of the function and sends back the value as a result
   

area = drawRectangle(3,5) #use the return value by setting a variable to the call
drawSquare(area, "!")

print("The area is " + str(area))

#or you can use it directly in another statement
print(drawRectangle(8,10))

