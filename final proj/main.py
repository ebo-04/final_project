import sys

sys.path.append("classes")
from classes.Books import Book
from classes.BorrowingOrders import BorrowingOrder
from classes.LibraryClients import *


def Main():
    print(
        "Main Menu:\n"
        "1.Clients\n"
        "2.Books\n"
        "3.Librarians\n"
        "4.Borrowing Orders\n"
        "5. Exit\n"
    )
    option = input("Inter the key number")
    option = int(option)
    if option in (1, 2, 3, 4, 5):

        if option == 1:
            Client.ClientsMenu()

        if option == 2:
            Book.BooksOptions()

        elif option == 3:
            Librarian.LibrariansOptions()

        elif option == 4:
            BorrowingOrder.OrdersMenu()

        elif option == 5:
            print("Exited successfully")

    else:
        print("Invalid input")
        Main()


Main()
