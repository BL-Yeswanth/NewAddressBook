import json


class JSONFileService:
    """
    UC15: Read and Write Address Book contacts using JSON File
    """

    FILE_NAME = "address_book.json"

    @staticmethod
    def write_to_json(address_book):
        if not address_book.contacts:
            print("No contacts available to write into JSON.")
            return

        data = []

        for contact in address_book.contacts:
            data.append({
                "first_name": contact.first_name,
                "last_name": contact.last_name,
                "address": contact.address,
                "city": contact.city,
                "state": contact.state,
                "zip_code": contact.zip_code,
                "phone_number": contact.phone_number,
                "email": contact.email
            })

        with open(JSONFileService.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

        print("Contacts successfully written to JSON file.")

    @staticmethod
    def read_from_json():
        try:
            with open(JSONFileService.FILE_NAME, "r") as file:
                data = json.load(file)

                print("\nContacts from JSON File:")
                for contact in data:
                    print(
                        f"{contact['first_name']} {contact['last_name']}, "
                        f"{contact['city']}, {contact['state']}, "
                        f"{contact['zip_code']}, "
                        f"{contact['phone_number']}, "
                        f"{contact['email']}"
                    )

        except FileNotFoundError:
            print("JSON file not found. No data to read.")
