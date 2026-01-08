class ViewPerson:
    """
    UC9: View persons by City or State
    Simple dictionary-based implementation
    """

    @staticmethod
    def view_by_city(address_books):
        city_person_map = {}

        for address_book in address_books.values():
            for contact in address_book.contacts:
                city = contact.city

                if city not in city_person_map:
                    city_person_map[city] = []

                city_person_map[city].append(contact)

        if not city_person_map:
            print("No persons found.")
            return

        print("\nPersons Grouped by City")
        for city, persons in city_person_map.items():
            print(f"\nCity: {city}")
            for person in persons:
                person.display()

    @staticmethod
    def view_by_state(address_books):
        state_person_map = {}

        for address_book in address_books.values():
            for contact in address_book.contacts:
                state = contact.state

                if state not in state_person_map:
                    state_person_map[state] = []

                state_person_map[state].append(contact)

        if not state_person_map:
            print("No persons found.")
            return

        print("\nPersons Grouped by State")
        for state, persons in state_person_map.items():
            print(f"\nState: {state}")
            for person in persons:
                person.display()
