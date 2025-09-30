counter = 0
# operators for math: +, -, *, /
counter = counter + 1
print(counter)
# PEMDAS applies
counter = counter + 6 * 3 #is not the same as (counter + 6) * 3
print(counter)
counter = counter / 3
print(counter)
print(counter - 5) # this time we're not saving to a variable -- just outputting the answer
print(counter)
# programmers are lazy, so there are some shortcuts
# the += (and similar) operator works just like these above do
counter += 100 #that's the same as counter = counter + 100
print(counter)
#-----  Taking input for numbers. ------
#Write code asking the user for some number, then do some math on it and output the results
cows = input("How many cows do you have? ")
print(cows)

# cows = cows - 10
# print("Now there are ", cows)
# Type casting -- now with validation (the try/catch blocks)
try:  #if there is an error in the code of the block below, it will jump to the 'except' part
    cows = int(cows) #turns the value of cows into an integer
    #if you want to allow decimals, use float(cows) instead --or whatever variable you're using.
except: #This block runs if the try block throws an error
    print("Ummm...you can't have that many cows.  I will give you ten...you're welcome.")
    cows = 10

print("That's good, but a pack of rustlers came by and now you have ten fewer")
cows = cows - 10
print("Now there are " + str(cows)) # str(...) converts it to a string
# This only works if the input is actually an integer. If the user types in something else (and they will) it will break

def getInt(q):
    print(q)

n = getInt("How many cows in the barnyard?")
n += 3
print(n)
    
