def getInt(prompt):
    goodInput = False
    while not goodInput:
        n = input(prompt)
        try:
            n = int(n)
            goodInput = True
        except:
            print("Please enter a whole number")
    return n

def getFloat(prompt):
    goodInput = False
    while not goodInput:
        n = input(prompt)
        try:
            n = float(n)
            goodInput = True
        except:
            print("Please enter a number (decimals OK)")
    return n
