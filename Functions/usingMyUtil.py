from myUtil import getInt, getFloat
someNum = getInt("How many cows in the barnyard?")
someOtherNum = getFloat("What's the temperature outside?")
total = someNum * someOtherNum
print("That's certain victory by " + str(total) + " points")
