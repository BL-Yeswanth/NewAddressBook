# UC1: Import required classes
from address_book import AddressBook
from contact import Contact
from edit_contact import EditContact
from delete_contact import DeleteContact
from address_book_system import AddressBookSystem   # UC6
from search_service import SearchService             # UC8
from view_person import ViewPerson                   # UC9
from count_person import CountPerson                 # UC10
from sort_person import SortPerson                   # UC12
from file_service import FileService    # UC13


class AddressBookMain:
    def __init__(self):
        # UC6: Create AddressBookSystem instead of single AddressBook
        self.system = AddressBookSystem()
        self.address_book = None

    def start(self):
        print("Welcome to Address Book Program")

        # UC6: Create / Select Address Book
        book_name = input("Enter Address Book Name: ")
        self.address_book = self.system.create_address_book(book_name)

        if not self.address_book:
            return

        # UC2 + UC5: Add multiple contacts
        while True:
            print("\nEnter Contact Details")

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

            self.address_book.add_contact(contact)

            choice = input("\nDo you want to add another contact? (yes/no): ").lower()
            if choice != "yes":
                break

        # UC3: Edit contact
        if input("\nDo you want to edit an existing contact? (yes/no): ").lower() == "yes":
            first_name = input("Enter First Name to edit: ")
            EditContact(self.address_book).edit_by_first_name(first_name)

        # UC4: Delete contact
        if input("\nDo you want to delete a contact? (yes/no): ").lower() == "yes":
            first_name = input("Enter First Name to delete: ")
            DeleteContact(self.address_book).delete_by_first_name(first_name)

        # UC8: Search
        if input("\nDo you want to search person by City or State? (yes/no): ").lower() == "yes":
            print("\n1. Search by City\n2. Search by State")
            option = input("Enter option: ")

            if option == "1":
                city = input("Enter City Name: ")
                results = SearchService.search_by_city(self.system.address_books, city)
            elif option == "2":
                state = input("Enter State Name: ")
                results = SearchService.search_by_state(self.system.address_books, state)
            else:
                results = []

            if results:
                for contact in results:
                    contact.display()
            else:
                print("No matching persons found.")

        # UC9: View persons
        if input("\nDo you want to view persons by City or State? (yes/no): ").lower() == "yes":
            print("\n1. View by City\n2. View by State")
            option = input("Enter option: ")

            if option == "1":
                ViewPerson.view_by_city(self.system.address_books)
            elif option == "2":
                ViewPerson.view_by_state(self.system.address_books)

        # UC10: Count persons
        if input("\nDo you want to count persons by City or State? (yes/no): ").lower() == "yes":
            print("\n1. Count by City\n2. Count by State")
            option = input("Enter option: ")

            if option == "1":
                CountPerson.count_by_city(self.system.address_books)
            elif option == "2":
                CountPerson.count_by_state(self.system.address_books)

        # =========================
        # UC11: Sort contacts by First Name
        # =========================
        if input("\nDo you want to sort contacts by First Name? (yes/no): ").lower() == "yes":
            sorted_contacts = sorted(
                self.address_book.contacts,
                key=lambda c: c.first_name.lower()
            )

            print("\nSorted Contacts by First Name:")
            for contact in sorted_contacts:
                print(contact)

        # =========================
        # UC12: Sort contacts by City / State / Zip
        # =========================
        if input("\nDo you want to sort contacts by City, State or Zip? (yes/no): ").lower() == "yes":
            print("\nSorting Options")
            print("1. Sort by City")
            print("2. Sort by State")
            print("3. Sort by Zip Code")

            option = input("Enter option (1/2/3): ")

            if option == "1":
                SortPerson.sort_by_city(self.address_book)
            elif option == "2":
                SortPerson.sort_by_state(self.address_book)
            elif option == "3":
                SortPerson.sort_by_zip(self.address_book)
            else:
                print("Invalid option selected.")
                
            
                # =========================
        # UC13: Read / Write Address Book using File IO
        # =========================
        file_choice = input(
            "\nDo you want to Read or Write contacts to file? (yes/no): "
        ).lower()

        if file_choice == "yes":
            print("\nFile Options")
            print("1. Write contacts to file")
            print("2. Read contacts from file")

            option = input("Enter option (1 or 2): ")

            if option == "1":
                FileService.write_to_file(self.address_book)
            elif option == "2":
                FileService.read_from_file()
            else:
                print("Invalid option selected.")


        # Display all contacts
        self.address_book.display_contacts()


if __name__ == "__main__":
    app = AddressBookMain()
    app.start()
