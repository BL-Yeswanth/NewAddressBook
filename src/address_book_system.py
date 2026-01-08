# UC6: Manage multiple Address Books using Dictionary
from address_book import AddressBook


class AddressBookSystem:
    def __init__(self):
        # UC6: Dictionary to store multiple address books
        self.address_books = {}

    def create_address_book(self, name):
        if name in self.address_books:
            print(f"Address Book '{name}' already exists.")
            return None

        self.address_books[name] = AddressBook()
        print(f"Address Book '{name}' created successfully.")
        return self.address_books[name]

    def get_address_book(self, name):
        return self.address_books.get(name)

    def display_address_books(self):
        if not self.address_books:
            print("No Address Books available.")
            return

        print("\nAvailable Address Books:")
        for name in self.address_books:
            print("-", name)
