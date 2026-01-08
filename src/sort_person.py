class SortPerson:
    """
    UC12: Sort contacts in the Address Book by
    City, State, or Zip Code using Python collections
    """

    @staticmethod
    def sort_by_city(address_book):
        if not address_book.contacts:
            print("No contacts available to sort.")
            return

        address_book.contacts.sort(
            key=lambda contact: contact.city.lower()
        )

        print("\nContacts Sorted by City")
        for contact in address_book.contacts:
            print(contact)

    @staticmethod
    def sort_by_state(address_book):
        if not address_book.contacts:
            print("No contacts available to sort.")
            return

        address_book.contacts.sort(
            key=lambda contact: contact.state.lower()
        )

        print("\nContacts Sorted by State")
        for contact in address_book.contacts:
            print(contact)

    @staticmethod
    def sort_by_zip(address_book):
        if not address_book.contacts:
            print("No contacts available to sort.")
            return

        address_book.contacts.sort(
            key=lambda contact: contact.zip_code
        )

        print("\nContacts Sorted by Zip Code")
        for contact in address_book.contacts:
            print(contact)
