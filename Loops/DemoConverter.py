print("This is a converter")

#control variable
shouldContinue = True
while(shouldContinue):
    cType = input("What would you like to convert (W)eight, or (T)emperature (Q to quit)? ")
    cType = cType[:1].lower()
    if (cType == "t"):
        print("Great. Now I'll convert temperature")
        print("Seriously...this part will be amazing when it's done.")
    elif(cType == "w"):
        print("But wait until you see the weight part!")
        print("See what I did there?")
    elif(cType == "q"):
        shouldContinue = False
    else:
        print("Sometimes I just don't get you.")
print("Goodbye.")