# UC1: Import required classes
from address_book import AddressBook
from contact import Contact
from edit_contact import EditContact
from delete_contact import DeleteContact
from address_book_system import AddressBookSystem   # UC6
from search_service import SearchService             # UC8
from view_person import ViewPerson                   # UC9
from count_person import CountPerson                 # UC10


class AddressBookMain:
    def __init__(self):
        # UC6: Create AddressBookSystem instead of single AddressBook
        self.system = AddressBookSystem()
        self.address_book = None

    def start(self):
        # UC1: Display Welcome Message
        print("Welcome to Address Book Program")

        # UC6: Create / Select Address Book
        book_name = input("Enter Address Book Name: ")
        self.address_book = self.system.create_address_book(book_name)

        # If address book already exists, stop safely
        if not self.address_book:
            return

        # UC2 + UC5: Add multiple contacts using while loop
        while True:
            print("\nEnter Contact Details")

            # UC1: Create Contact using console input
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            address = input("Address: ")
            city = input("City: ")
            state = input("State: ")
            zip_code = input("Zip Code: ")
            phone_number = input("Phone Number: ")
            email = input("Email: ")

            contact = Contact(
                first_name,
                last_name,
                address,
                city,
                state,
                zip_code,
                phone_number,
                email
            )

            # UC2: Add contact to address book
            self.address_book.add_contact(contact)

            choice = input(
                "\nDo you want to add another contact? (yes/no): "
            ).lower()

            if choice != "yes":
                break

        # UC3: Edit contact
        edit_choice = input(
            "\nDo you want to edit an existing contact? (yes/no): "
        ).lower()

        if edit_choice == "yes":
            first_name = input("Enter First Name to edit: ")
            editor = EditContact(self.address_book)
            editor.edit_by_first_name(first_name)

        # UC4: Delete contact
        delete_choice = input(
            "\nDo you want to delete a contact? (yes/no): "
        ).lower()

        if delete_choice == "yes":
            first_name = input("Enter First Name to delete: ")
            deleter = DeleteContact(self.address_book)
            deleter.delete_by_first_name(first_name)

        # UC8: Search person by City or State across multiple Address Books
        search_choice = input(
            "\nDo you want to search person by City or State? (yes/no): "
        ).lower()

        if search_choice == "yes":
            print("\nSearch Options")
            print("1. Search by City")
            print("2. Search by State")

            option = input("Enter option (1 or 2): ")

            if option == "1":
                city = input("Enter City Name: ")
                results = SearchService.search_by_city(
                    self.system.address_books, city
                )

            elif option == "2":
                state = input("Enter State Name: ")
                results = SearchService.search_by_state(
                    self.system.address_books, state
                )

            else:
                results = []
                print("Invalid option selected.")

            if results:
                print("\nSearch Results:")
                for contact in results:
                    contact.display()
            else:
                print("No matching persons found.")

        # UC9: View persons by City or State (Dictionary-based view)
        view_choice = input(
            "\nDo you want to view persons by City or State? (yes/no): "
        ).lower()

        if view_choice == "yes":
            print("\nView Options")
            print("1. View by City")
            print("2. View by State")

            option = input("Enter option (1 or 2): ")

            if option == "1":
                ViewPerson.view_by_city(self.system.address_books)
            elif option == "2":
                ViewPerson.view_by_state(self.system.address_books)
            else:
                print("Invalid option selected.")

        # UC10: Count number of persons by City or State
        count_choice = input(
            "\nDo you want to count persons by City or State? (yes/no): "
        ).lower()

        if count_choice == "yes":
            print("\nCount Options")
            print("1. Count by City")
            print("2. Count by State")

            option = input("Enter option (1 or 2): ")

            if option == "1":
                CountPerson.count_by_city(self.system.address_books)
            elif option == "2":
                CountPerson.count_by_state(self.system.address_books)
            else:
                print("Invalid option selected.")

        # UC2 / UC3 / UC4: Display all contacts
        self.address_book.display_contacts()


# Program execution starts here
if __name__ == "__main__":
    app = AddressBookMain()
    app.start()
