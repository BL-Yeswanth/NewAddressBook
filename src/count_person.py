class CountPerson:
    """
    UC10: Count number of persons by City or State
    """

    @staticmethod
    def count_by_city(address_books):
        city_count = {}

        for address_book in address_books.values():
            for contact in address_book.contacts:
                city = contact.city

                if city not in city_count:
                    city_count[city] = 0

                city_count[city] += 1

        if not city_count:
            print("No persons found.")
            return

        print("\nPerson Count by City")
        for city, count in city_count.items():
            print(f"{city} -> {count}")

    @staticmethod
    def count_by_state(address_books):
        state_count = {}

        for address_book in address_books.values():
            for contact in address_book.contacts:
                state = contact.state

                if state not in state_count:
                    state_count[state] = 0

                state_count[state] += 1

        if not state_count:
            print("No persons found.")
            return

        print("\nPerson Count by State")
        for state, count in state_count.items():
            print(f"{state} -> {count}")
