class FileService:
    """
    UC13: Read and Write Address Book contacts using File IO
    """

    FILE_NAME = "address_book.txt"

    @staticmethod
    def write_to_file(address_book):
        if not address_book.contacts:
            print("No contacts to write into file.")
            return

        with open(FileService.FILE_NAME, "w") as file:
            for contact in address_book.contacts:
                file.write(
                    f"{contact.first_name},"
                    f"{contact.last_name},"
                    f"{contact.address},"
                    f"{contact.city},"
                    f"{contact.state},"
                    f"{contact.zip_code},"
                    f"{contact.phone_number},"
                    f"{contact.email}\n"
                )

        print("Contacts successfully written to file.")

    @staticmethod
    def read_from_file():
        try:
            with open(FileService.FILE_NAME, "r") as file:
                print("\nContacts from File:")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("File not found. No data to read.")
