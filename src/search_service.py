class SearchService:
    """
    UC8: Search person by city or state across multiple address books
    """

    @staticmethod
    def search_by_city(address_books, city):
        results = []

        for book_name, address_book in address_books.items():
            for contact in address_book.contacts:
                if contact.city.lower() == city.lower():
                    results.append(contact)

        return results

    @staticmethod
    def search_by_state(address_books, state):
        results = []

        for book_name, address_book in address_books.items():
            for contact in address_book.contacts:
                if contact.state.lower() == state.lower():
                    results.append(contact)

        return results
