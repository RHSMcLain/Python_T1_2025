n = 1000
while n >= 0:  
    print(n, end="...")
    n -= 3
# 10...9...8...7...6
print("Done")
# --- Comparison Operator
# '<' less than
# '>' greater than
# '==' test if they are equal
# '<='
# '>='
# '!=' not equal
# 'not' means ... not 
#---------------------------------------------------------
#------ While loops controlled by a Boolean (True/False)
#---------------------------------------------------------

shouldContinue = True
while shouldContinue:
    answer = input("What is the answer?")
    if (answer == "42"):
        shouldContinue = False
print("Finally you got it right")