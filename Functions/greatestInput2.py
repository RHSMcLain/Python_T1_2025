#loop as long as the user wants
#take input
#validate it as a number or quit condition
#if it's a number, check if it is the new largest and store it as needed
#if quit condition, return the largest value

def largestInput():
    shouldContinue = True
    largestValue = None
    while shouldContinue:
        n = input("Enter a number (q to quit): ")
       
        try:
            n = int(n) 
            if (largestValue == None or n > largestValue):
                largestValue = n
        except:
            if (n == "q"):
                shouldContinue = False
    return largestValue

print(largestInput())


