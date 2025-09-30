from myUtil import getInt
def largestInput():
    shouldContinue = True
    largestVal = None
    while shouldContinue:
        n = getInt("Enter a number: ")
        if (largestVal == None or n > largestVal):
            largestVal = n
        keepGoing = input("Do you want to enter more? (Y/N)")
        keepGoing = keepGoing[:1].lower()
        shouldContinue = keepGoing != "n"
    return largestVal
greatest = largestInput()
print(f"The biggest value entered was {greatest}")

    