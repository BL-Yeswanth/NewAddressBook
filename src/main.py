from address_book import AddressBook
from contact import Contact


class AddressBookMain:
    def __init__(self):
        # UC1: Create Address Book
        self.address_book = AddressBook()

    def start(self):
        # UC1: Display Welcome Message
        print("Welcome to Address Book Program")

        # UC2: Add multiple contacts using while loop
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

            # UC2: Ask user if they want to continue
            choice = input(
                "\nDo you want to add another contact? (yes/no): "
            ).lower()

            if choice != "yes":
                break

        # UC2: Display all added contacts
        self.address_book.display_contacts()


# Program execution starts here
if __name__ == "__main__":
    app = AddressBookMain()
    app.start()
