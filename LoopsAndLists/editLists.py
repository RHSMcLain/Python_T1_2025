# this program will show looping through lists with indexes, and allowing the user to edit the list easily
books = []

def addBook():
    #ask for a new book title and add it to the list
    newTitle = input("What book did you read?")
    books.append(newTitle)

def listBooks():
    # for book in books:
    #     print(book)
    # to get the length of the list (number of items, use the len() function)
    print(len(books))
    for i in range(len(books)):
        print(str(i + 1) + ": " + books[i])


def editBook():
    #what do we need?
    #TODO: refactor for a select books function to be used by edit and remove book functions
    listBooks()
    print("-----")
    bookToEdit = input("Which one would you like to change?")
    #TODO: Validate input as an int in the range of the list
    bookToEdit = int(bookToEdit) -1
    print(" WE will edit book " + books[bookToEdit])
    
while True:
    #menu part
    action = input("What would you like to do? (A)dd book, (L)ist books, (E)dit book , (Q)uit>> ")
    action = action[:1].lower()
    if (action == "a"):
        addBook()
    elif action == "l":
        listBooks()
    elif action == "e":
        editBook()    
    elif action == "q":
        break
    else:
        print("I don't know that command yet. Try again.")