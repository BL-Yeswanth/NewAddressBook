# UC3: Edit existing contact by first name
class EditContact:
    def __init__(self, address_book):
        self.address_book = address_book

    def edit_by_first_name(self, first_name):
        for contact in self.address_book.contacts:
            if contact.first_name == first_name:
                print("\nContact found. Enter new details:")

                contact.last_name = input("New Last Name: ")
                contact.address = input("New Address: ")
                contact.city = input("New City: ")
                contact.state = input("New State: ")
                contact.zip_code = input("New Zip Code: ")
                contact.phone_number = input("New Phone Number: ")
                contact.email = input("New Email: ")

                print("Contact updated successfully.")
                return

        print("Contact not found.")
