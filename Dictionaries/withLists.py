import shelve
classes = {}
selectedClass = ""
def addClass():
    newClassName = input("What is the class name?")
    #validate -- not only whitespaces and not already in the list
    newClassName = newClassName.strip()
    if (len(newClassName) == 0):
        print("please try again: that was only spaces.")
        return
    if newClassName in classes:
        print("You already have that class.")
        return
    classes[newClassName] = []
    print(f"{newClassName} added")
    return
def printClasses():
    print("<<< List of Classes  >>>")
    for key in classes:
        print(key)

def selectClass():
    global selectedClass
    selection = input("Which Class do you want to focus on?")
    if (selection not in classes):
        print("We don't have that class")
    else:
        selectedClass = selection

def addStudent(studentName):
    classes[selectedClass].append(studentName)


def mainMenu():
    shouldContinue = True
    while shouldContinue:
        print("<<<--------------->>>")
        cmd = input('What would you like to do? (A)dd class, (S)elect a class, (Q)uit')
        cmd = cmd.lower()[:1]
        if (cmd == 'a'):
            addClass()
        elif (cmd == 'q'):
            shouldContinue = False
        elif (cmd == 's'):
            printClasses()
            # selectClass()

mainMenu()
print("Goodbye")

