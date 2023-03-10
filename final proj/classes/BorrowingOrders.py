from Books import Book
from LibraryClients import *
from datetime import date


class BorrowingOrder:
    def __init__(self, id, date, client_id, book_id, librarian_id, status):
        self.id = id
        self.date = date
        self.client_id = client_id
        self.book_id = book_id
        self.librarian_id = librarian_id
        self.status = status

    ordersList = []

    counter = 0

    def OrdersMenu():

        val = False
        while not val:
            print(
                "Borrowing Orders Menu:\n"
                "1. Borrow a book\n"
                "2. Return a book\n"
                "3. Cancel order\n"
                "4. View order\n"
                "5. list client orders\n"
                "6. list all orders\n"
                "7. Total borrowed orders\n"
                "8. Return to main menu\n"
            )
            option = input("Inter the key number")
            option = int(option)
            if option in (1, 2, 3, 4, 5, 6, 7, 8):
                if option == 1:
                    BorrowingOrder.BorrowBook()

                elif option == 2:
                    BorrowingOrder.ReturnBook()

                elif option == 3:
                    BorrowingOrder.CancelOrder()

                elif option == 4:
                    BorrowingOrder.ViewOrder()

                elif option == 5:
                    BorrowingOrder.ClientOrders()

                elif option == 6:
                    BorrowingOrder.ListOrders()

                elif option == 7:
                    BorrowingOrder.TotalOrders()

                elif option == 8:
                    val = True

            else:
                print("\nInvalid input")

    def SearchOrder(id):

        for order in BorrowingOrder.ordersList:
            if order.id == id:
                return BorrowingOrder.ordersList.index(order)
        return -1

    def ActiveOrders():

        print("\nActive orders: ")
        print(
            "\nBorrowing id\t  Order date\t Client id\t Book id\t Librarian id\t Status"
        )
        for order in BorrowingOrder.ordersList:
            if order.status == "Active":
                print(
                    order.id,
                    "\t",
                    order.date,
                    "\t",
                    order.client_id,
                    "\t",
                    order.book_id,
                    "\t",
                    order.librarian_id,
                    "\t",
                    order.status,
                )

    def BorrowBook():

        librarian_id = input("\nEnter your librarian id: ")
        librarianIndex = Librarian.SearchLibrarian(librarian_id)
        if librarianIndex != -1:
            Book.ActiveBooks()
            book_id = input("\nEnter book id you want to borrow: ")
            bookIndex = Book.SearchBook(book_id)
            if bookIndex != -1:
                if Book.bookList[bookIndex].status == "Active":
                    client_id = input("\nEnter client id: ")
                    if Client.SearchClient(client_id) != -1:
                        id = str(BorrowingOrder.counter + 1)
                        BorrowingOrder.counter = BorrowingOrder.counter + 1
                        orderDate = date.today()
                        status = "Active"

                        newOrder = BorrowingOrder(
                            id, orderDate, client_id, book_id, librarian_id, status
                        )
                        BorrowingOrder.ordersList.append(newOrder)
                        print("\nBook borrowed successfully\n")

                        Book.bookList[bookIndex].status = "Inactive"

                    else:
                        print("\nThere is no client with this id.")
                else:
                    print("\nThis book is inactive.")
            else:
                print("\nThere is no book with this id.")
        else:
            print("\nThere is no librarian with this id.")

        val = False
        while not val:
            print("Do you want to add another borrowing order?\n" "1. Yes\n" "2. No\n")
            reins = input("Inter the key number")
            reins = int(reins)
            if reins in (1, 2):
                if reins == 1:
                    BorrowingOrder.BorrowBook()
                elif reins == 2:
                    val = True
            else:
                print("Invalid input\n")

    def ReturnBook():

        BorrowingOrder.ActiveOrders()
        borrowing_id = input(
            "\nEnter borrowing id you want to return:\n" "Borrowing id: "
        )
        index = BorrowingOrder.SearchOrder(borrowing_id)
        if index != -1:
            BorrowingOrder.ordersList[index].status = "Expired"
            book_index = Book.SearchBook(BorrowingOrder.ordersList[index].book_id)
            Book.bookList[book_index].status = "Active"
            print("\nBook returned successfully\n")
        else:
            print("\nThere is no borrowing order with this id\n")

        val = False
        while not val:
            print("Do you want to add another return order?\n" "1. Yes\n" "2. No\n")
            reins = input("Inter the key number")
            reins = int(reins)
            if reins in (1, 2):
                if reins == 1:
                    BorrowingOrder.ReturnBook()
                elif reins == 2:
                    val = True
            else:
                print("Invalid input\n")

    def CancelOrder():

        BorrowingOrder.ActiveOrders()
        borrowing_id = input(
            "\nEnter borrowing id you want to cancel:\n" "Borrowing id: "
        )
        index = BorrowingOrder.SearchOrder(borrowing_id)
        if index != -1:
            BorrowingOrder.ordersList[index].status = "Canceled"
            book_index = Book.SearchBook(BorrowingOrder.ordersList[index].book_id)
            Book.bookList[book_index].status = "Active"
            print("\nOrder canceled successfully\n")
        else:
            print("\nThere is no borrowing order with this id\n")

        val = False
        while not val:
            print("Do you want to cancel another order?\n" "1. Yes\n" "2. No\n")
            reins = input("Inter the key number")
            reins = int(reins)
            if reins in (1, 2):
                if reins == 1:
                    BorrowingOrder.ReturnBook()
                elif reins == 2:
                    val = True
            else:
                print("\nInvalid input\n")

    def ViewOrder():

        borrowing_id = input(
            "\nEnter a borrowing id to view its data\n" "Borrowing id: "
        )
        index = BorrowingOrder.SearchOrder(borrowing_id)

        if index != -1:
            print(
                "\nBorrowing id\t  Order date\t Client id\t Book id\t Librarian id\t Status"
            )
            print(
                BorrowingOrder.ordersList[index].id,
                "\t",
                BorrowingOrder.ordersList[index].date,
                "\t",
                BorrowingOrder.ordersList[index].client_id,
                "\t",
                BorrowingOrder.ordersList[index].book_id,
                "\t",
                BorrowingOrder.ordersList[index].librarian_id,
                "\t",
                BorrowingOrder.ordersList[index].status,
            )

        else:
            print("\nInvalid input")

        val = False
        while not val:
            print("Do you want to view another order?\n" "1. Yes\n" "2. No\n")
            option = input("Inter the key number")
            option = int(option)
            if option in (1, 2):
                if option == 1:
                    Book.ViewBook()
                elif option == 2:
                    val = True
            else:
                print("Invalid input\n")

    def ListOrders():

        if len(BorrowingOrder.ordersList) > 0:
            print(
                "\nBorrowing id\t  Order date\t Client id\t Book id\t Librarian id\t Status"
            )
            for order in BorrowingOrder.ordersList:
                print(
                    order.id,
                    "\t",
                    order.date,
                    "\t",
                    order.client_id,
                    "\t",
                    order.book_id,
                    "\t",
                    order.librarian_id,
                    "\t",
                    order.status,
                )
        else:
            print("\nThere are no registered orders yet")

    def TotalOrders():

        active, expired, canceled = 0, 0, 0
        for order in BorrowingOrder.ordersList:
            if order.status == "Active":
                active = active + 1
            elif order.status == "Expired":
                expired = expired + 1
            else:
                canceled = canceled + 1

        print(
            "\nTotal active orders = ",
            active,
            "\nTotal expired orders = ",
            expired,
            "\nTotal canceled orders = ",
            canceled,
        )

    def ClientOrders():

        id = input("\nEnter client id: ")
        index = Client.SearchClient(id)
        if index != -1:
            print(
                "\nBorrowing id\t  Order date\t Client id\t Book id\t Librarian id\t Status"
            )
            for order in BorrowingOrder.ordersList:
                if order.client_id == id:
                    print(
                        order.id,
                        "\t",
                        order.date,
                        "\t",
                        order.client_id,
                        "\t",
                        order.book_id,
                        "\t",
                        order.librarian_id,
                        "\t",
                        order.status,
                    )

