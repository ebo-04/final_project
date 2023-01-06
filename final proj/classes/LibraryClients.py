class Client:
    def __init__(self, id, full_name, age, id_no, phone_number):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.phone_number = phone_number

    ClientsList = []

    def ClientsMenu():

        val = False
        while not val:
            print(
                "Clients Menu:\n"
                "1.Add client\n"
                "2.Delete client\n"
                "3.View client\n"
                "4.List all clients\n"
                "5.Return to main menu\n"
            )
            option = input("Inter the key number")
            option = int(option)
            if option in (1, 2, 3, 4, 5):

                if option == 1:
                    Client.AddClient()

                elif option == 2:
                    Client.DeleteClient()

                elif option == 3:
                    Client.ViewClient()

                elif option == 4:
                    Client.ListClients()

                elif option == 5:
                    val = True

            else:
                print("Invalid input")

    def SearchClient(id):

        for client in Client.ClientsList:
            if client.id == id:
                return Client.ClientsList.index(client)
        return -1

    def AddClient():

        id = input("\nEnter your id: ")
        if id.strip() != "" and id.isdigit() and Client.SearchClient(id) == -1:
            full_name = input("Enter your full name: ")
            if full_name.strip() != "" and full_name.replace(" ", "").isalpha():
                age = input("Enter your age: ")
                if age.strip() != "" and age.isdigit():
                    id_no = input("Enter your id number: ")
                    if id_no.strip() != "" and id_no.isdigit():
                        phone_number = input("Enter your phone number: ")
                        if phone_number.strip() != "" and phone_number.isdigit():

                            newClient = Client(id, full_name, age, id_no, phone_number)
                            Client.ClientsList.append(newClient)
                            print("\nClient added\n")

                        else:
                            print("\nInvalid input\n")
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
            print("Do you wanna add other client?\n" "1. Yes\n" "2. No\n")
            reins = input("Inter option key")
            reins = int(reins)
            if reins in (1, 2):
                if reins == 1:
                    Client.AddClient()
                elif reins == 2:
                    val = True
            else:
                print("Invalid input")

    def DeleteClient():
        print("Enter client Id you wanna delete")
        clientId = input("The ID:")
        index = Client.SearchClient(clientId)
        if index != -1:
            Client.ClientsList.pop(index)
            print("Client deleted successfully\n")
        else:
            print("Client not found")

        val = False
        while not val:
            print("Do you want to delete another client?\n" "1. Yes\n" "2. No\n")
            reins = input("Inter the key number")
            reins = int(reins)
            if reins in (1, 2):
                if reins == 1:
                    Client.DeleteClient()
                elif reins == 2:
                    val = True
            else:
                print("Invalid input")

    def ViewClient():
        print("Enter client Id to view clients data\n")
        id = input("The Id:")
        index = Client.SearchClient(id)
        if index != -1:
            print(
                "\nClient id\t Client name\t Client age\t Client ID\t Client phone number"
            )
            print(
                Client.ClientsList[index].id,
                "\t",
                Client.ClientsList[index].full_name,
                "\t",
                Client.ClientsList[index].age,
                "\t",
                Client.ClientsList[index].id_no,
                "\t",
                Client.ClientsList[index].phone_number,
            )

        else:
            print("\nInvalid input")

        val = False
        while not val:
            print("Do you wanna view other client?\n" "1. Yes\n" "2. No\n")
            reins = input("Inter the key number")
            reins = int(reins)
            if reins in (1, 2):
                if reins == 1:
                    Client.ViewClient()
                elif reins == 2:
                    val = True
            else:
                print("Invalid input")

    def ListClients():

        if len(Client.ClientsList) > 0:
            print("\nClient id\t Client name\t Client age\t Client ID\t Client phone")
            for client in Client.ClientsList:
                print(
                    client.id,
                    "\t",
                    client.full_name,
                    "\t",
                    client.age,
                    "\t",
                    client.id_no,
                    "\t",
                    client.phone_number,
                )
        else:
            print("\nThere are'nt registered clients")


class Librarian:
    def __init__(self, id, full_name, age, id_no, emplyment_type):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.emplyment_type = emplyment_type

    librarianList = []

    def LibrariansOptions():

        val = False
        while not val:
            print(
                "Librarians Menu:\n"
                "1.Add librarian\n"
                "2.Delete librarian\n"
                "3.View librarian\n"
                "4.List librarians\n"
                "5.Back to main menu\n"
            )
            option = input("Inter the key number")
            option = int(option)
            if option in (1, 2, 3, 4, 5):

                if option == 1:
                    Librarian.AddLibrarian()

                elif option == 2:
                    Librarian.DeleteLibrarian()

                elif option == 3:
                    Librarian.ViewLibrarian()

                elif option == 4:
                    Librarian.ListLibrarians()

                elif option == 5:
                    val = True

            else:
                print("\nInvalid input")

    def SearchLibrarian(id):

        for librarian in Librarian.librarianList:
            if librarian.id == id:
                return librarian.librarianList.index(librarian)
        return -1

    def AddLibrarian():

        id = input("\nEnter librarian id: ")
        if id.strip() != "" and id.isdigit() and Librarian.SearchLibrarian(id) == -1:
            full_name = input("Enter librarian full name: ")
            if full_name.strip() != "" and full_name.replace(" ", "").isalpha():
                age = input("Enter librarian age: ")
                if age.strip() != "" and age.isdigit():
                    id_no = input("Enter librarian id number: ")
                    if id_no.strip() != "" and id_no.isdigit():
                        print(
                            "Enter librarian emplyment type (Enter 1 or 2):\n"
                            "1. Full time\n"
                            "2. Part time\n"
                        )
                        emplyment_type = input("Inter type key:")
                        emplyment_type = int(emplyment_type)
                        if emplyment_type in (1, 2):

                            if emplyment_type == 1:
                                emplyment_type = "Full"

                                newlibrarian = Librarian(
                                    id, full_name, age, id_no, emplyment_type
                                )
                                Librarian.librarianList.append(newlibrarian)
                                print("\nLibrarian added successfully\n")

                            elif emplyment_type == 2:
                                emplyment_type = "Part"

                                newlibrarian = Librarian(
                                    id, full_name, age, id_no, emplyment_type
                                )
                                Librarian.librarianList.append(newlibrarian)
                                print("\nLibrarian added successfully\n")

                        else:
                            print("\nInvalid input\n")
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
            print("Do you want to add another librarian?\n" "1. Yes\n" "2. No\n")
            reins = input("Enter choice key:")
            reins = int(reins)
            if reins in (1, 2):
                if reins == 1:
                    Librarian.AddLibrarian()
                elif reins == 2:
                    val = True
            else:
                print("Invalid input\n")

    def DeleteLibrarian():

        librarianId = input("\nEnter the librarian id you want to delete.\n" "id: ")
        index = Librarian.SearchLibrarian(librarianId)
        if index != -1:
            Librarian.librarianList.pop(index)
            print("\nLibrarian deleted successfully\n")
        else:
            print("\nThere is no librarian with this id\n")

        val = False
        while not val:
            print("Do you want to delete another librarian?\n" "1. Yes\n" "2. No\n")
            reins = input("Inter answer key:")
            reins = int(reins)
            if reins in (1, 2):
                if reins == 1:
                    Librarian.DeleteLibrarian()
                elif reins == 2:
                    val = True
            else:
                print("Invalid input\n")

    def ViewLibrarian():

        id = input("\nEnter a librarian id to view its data\n" "id: ")
        index = Librarian.SearchLibrarian(id)

        if index != -1:
            print(
                "Librarian id\t Librarian name\t Librarian age\t Librarian ID\t Librarian emplyment type"
            )
            print(
                Librarian.librarianList[index].id,
                "\t",
                Librarian.librarianList[index].full_name,
                "\t",
                Librarian.librarianList[index].age,
                "\t",
                Librarian.librarianList[index].id_no,
                "\t",
                Librarian.librarianList[index].emplyment_type,
            )

        else:
            print("Invalid input")

        val = False
        while not val:
            print("Do you want to view another librarian" "1. Yes\n" "2. No\n")
            reins = input("Enter choice key:")
            reins = int(reins)
            if reins in (1, 2):
                if reins == 1:
                    Librarian.ViewLibrarian()
                elif reins == 2:
                    val = True
            else:
                print("Invalid input\n")

    def ListLibrarians():

        if len(Librarian.librarianList) > 0:
            print(
                "\nLibrarian id\t Librarian name\t Librarian age\t Librarian ID\t Librarian emplyment type"
            )
            for librarian in Librarian.librarianList:
                print(
                    librarian.id,
                    "\t",
                    librarian.full_name,
                    "\t",
                    librarian.age,
                    "\t",
                    librarian.id_no,
                    "\t",
                    librarian.emplyment_type,
                )
        else:
            print("\nThere are no registered librarians ")
