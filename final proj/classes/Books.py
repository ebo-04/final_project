class Book:
    def __init__(self, id, title, description, author, status):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.status = status

    BookList = []

    def SearchBook(id):

        for book in Book.BookList:
            if book.id == id:
                return book.BookList.index(book)
        return -1

    def ActiveBooks():

        print("\nActive Books:")
        print("\nBook id\t Book title\t Book description\t Book author\t Book status")
        for book in Book.BookList:
            if book.status == "Active":
                print(
                    book.id,
                    "\t",
                    book.title,
                    "\t",
                    book.description,
                    "\t",
                    book.author,
                    "\t",
                    book.status,
                )

    def AddBook():

        id = input("\nEnter book id: ")
        if id.strip() != "" and id.isdigit() and Book.SearchBook(id) == -1:
            title = input("Enter book title: ")
            if title.strip() != "":
                description = input("Enter book description: ")
                if description.strip() != "":
                    author = input("Enter book author: ")
                    if author.strip() != "" and author.replace(" ", "").isalpha():
                        status = "Active"

                        newBook = Book(id, title, description, author, status)
                        Book.BookList.append(newBook)
                        print("\nBook added successfully\n")

                    else:
                        print("\nInvalid input\n")
                else:
                    print("\nInvalid input\n")
            else:
                print("\nInvalid input\n")
        else:
            print("\nInvalid input\n")

        val = False
        while not val:

            again = input(
                "Do you want to add another book?\n"
                "1. Yes\n"
                "2. No\n"
                "Your choice: "
            )
            if again == "1":
                Book.AddBook()
            elif again == "2":
                val = True
            else:
                print("\nInvalid input\n")

    def DeleteBook():

        bookId = input("\nEnter the book id you want to delete.\n" "id: ")
        index = Book.SearchBook(bookId)
        if index != -1:
            Book.BookList.pop(index)
            print("\nBook deleted successfully\n")
        else:
            print("\nThere is no book with this id\n")

        val = False
        while not val:

            again = input(
                "Do you want to delete another book?\n"
                "1. Yes\n"
                "2. No\n"
                "Your choice: "
            )
            if again == "1":
                Book.DeleteBook()
            elif again == "2":
                val = True
            else:
                print("\nInvalid input\n")

    def ViewBook():

        id = input("\nEnter a book id to view its data\n" "id: ")
        index = Book.SearchBook(id)

        if index != -1:
            print("Book id\t Book title\t Book description\t Book author\t Book status")
            print(
                Book.BookList[index].id,
                "\t",
                Book.BookList[index].title,
                "\t",
                Book.BookList[index].description,
                "\t",
                Book.BookList[index].author,
                "\t",
                Book.BookList[index].status,
            )

        else:
            print("\nInvalid input")

        val = False
        while not val:

            choice = input(
                "\nDo you want to view another book:\n"
                "1. Yes\n"
                "2. No\n"
                "Your choice: "
            )
            if choice == "1":
                Book.ViewBook()
            elif choice == "2":
                val = True
            else:
                print("Invalid input\n")

    def ListBooks():

        if len(Book.BookList) > 0:
            print(
                "\nBook id\t Book title\t Book description\t Book author\t Book status"
            )
            for book in Book.BookList:
                print(
                    book.id,
                    "\t",
                    book.title,
                    "\t",
                    book.description,
                    "\t",
                    book.author,
                    "\t",
                    book.status,
                )
        else:
            print("\nThere are no books yet")

    def AvailableBooks():

        active = 0
        for book in Book.BookList:
            if book.status == "Active":
                active = active + 1
        print("\nAvailable books number is = ", active)

    def BorrowedBooks():

        inactive = 0
        for book in Book.BookList:
            if book.status == "Inactive":
                inactive = inactive + 1
        print("\nBorrowed books number is= ", inactive)

    def BooksOptions():

        val = False
        while not val:
            print(
                "Books Options:\n"
                "1. Add book\n"
                "2. View book\n"
                "3. List all books"
                "4. Delete book\n"
                "5. Available books number\n"
                "6. Borrowed books number\n"
                "7. Back to main menu\n"
            )
            option = input("\nYour choice: ")
            option = int(option)
            if option in (1, 2, 3, 4, 5, 6, 7):
                if option == 1:
                    Book.AddBook()

                elif option == 2:
                    Book.ViewBook()

                elif option == 3:
                    Book.ListBooks()

                elif option == 4:
                    Book.DeleteBook()

                elif option == 5:
                    Book.AvailableBooks()

                elif option == 6:
                    Book.BorrowedBooks()

                elif option == 7:
                    val = True

            else:
                print("\nInvalid input")

