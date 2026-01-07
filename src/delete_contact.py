# UC4: Ability to delete a person using first name
class DeleteContact:
    def __init__(self, address_book):
        self.address_book = address_book

    def delete_by_first_name(self, first_name):
        for contact in self.address_book.contacts:
            if contact.first_name.lower() == first_name.lower():
                self.address_book.contacts.remove(contact)
                print(f"\nContact '{first_name}' deleted successfully.")
                return

        print(f"\nContact '{first_name}' not found.")
