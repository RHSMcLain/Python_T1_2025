import shelve
# this program will show looping through lists with indexes, and allowing the user to edit the list easily
books = []

def saveFile():
    shelf = shelve.open("booksList")
    shelf['books'] = books
    shelf.close()

def openFile():
    global books
    shelf = shelve.open("booksList")
    try:
        books = shelf['books']
    except:
        books = []
    shelf.close()


def addBook():
    #ask for a new book title and add it to the list
    newTitle = input("What book did you read?")
    books.append(newTitle)
    saveFile()

def listBooks():
    # for book in books:
    #     print(book)
    # to get the length of the list (number of items, use the len() function)
    print(len(books))
    for i in range(len(books)):
        print(str(i + 1) + ": " + books[i])

#-----------------------
#. Your Job: Write a 'selectBook' function that 
#  returns the index of the book the user selects
#=========================
def selectBook():
    listBooks()
    print("-----")
    bookToEdit = input("Which one would you like to change?")
    #TODO: Validate input as an int in the range of the list
    bookToEdit = int(bookToEdit) -1
    return bookToEdit #the number that represents the index of the chosen book

def deleteBook():
    bookToDelete = selectBook()
    deletedBook = books.pop(bookToDelete)
    print('We deleted ' + deletedBook)
    saveFile()

def editBook():
    
    bookToEdit = selectBook()
    print(" We will edit book " + books[bookToEdit])
    newTitle = input("What would you like to change the title to? ")
    books[bookToEdit] = newTitle
    print("Done: " + books[bookToEdit])
    saveFile()

#-----------------------
# Start of Main Program
#-----------------------
openFile() 
while True:
    #menu part
    action = input("What would you like to do? (A)dd book, (L)ist books, (E)dit book, (D)elete book , (Q)uit>> ")
    action = action[:1].lower()
    if (action == "a"):
        addBook()
    elif action == "l":
        listBooks()
    elif action == "e":
        editBook()  
    elif action == "d":
        deleteBook()  
    elif action == "q":
        break
    else:
        print("I don't know that command yet. Try again.")