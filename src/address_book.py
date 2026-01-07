from contact import Contact


class AddressBook:
    """
    UC2: Manages multiple contacts in the Address Book
    """

    def __init__(self):
        # UC1: Create Address Book with empty contact list
        self.contacts = []

    def add_contact(self, contact):
        """
        UC2: Add a new contact to the address book
        """
        self.contacts.append(contact)
        print("Contact added successfully.")

    def display_contacts(self):
        """
        UC2: Display all contacts in the address book
        """
        if not self.contacts:
            print("No contacts available.")
            return

        print("\n----- Contact List -----")
        for contact in self.contacts:
            contact.display()
            print("-" * 40)
