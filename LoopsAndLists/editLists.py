# this program will show looping through lists with indexes, and allowing the user to edit the list easily
books = []

def addBook():
    #ask for a new book title and add it to the list
    newTitle = input("What book did you read?")
    books.append(newTitle)

def listBooks():
    for book in books:
        print(book)

while True:
    #menu part
    action = input("What would you like to do? (A)dd book, (L)ist books , (Q)uit>> ")
    action = action[:1].lower()
    if (action == "a"):
        addBook()
    elif action == "l":
        listBooks()
    elif action == "q":
        break
    else:
        print("I don't know that command yet. Try again.")