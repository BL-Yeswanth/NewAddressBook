import csv


class CSVFileService:
    """
    UC14: Read and Write Address Book contacts using CSV File
    """

    FILE_NAME = "address_book.csv"

    @staticmethod
    def write_to_csv(address_book):
        if not address_book.contacts:
            print("No contacts available to write into CSV.")
            return

        with open(CSVFileService.FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)

            # CSV Header
            writer.writerow([
                "First Name", "Last Name", "Address",
                "City", "State", "Zip",
                "Phone Number", "Email"
            ])

            # Write contact data
            for contact in address_book.contacts:
                writer.writerow([
                    contact.first_name,
                    contact.last_name,
                    contact.address,
                    contact.city,
                    contact.state,
                    contact.zip_code,
                    contact.phone_number,
                    contact.email
                ])

        print("Contacts successfully written to CSV file.")

    @staticmethod
    def read_from_csv():
        try:
            with open(CSVFileService.FILE_NAME, mode="r") as file:
                reader = csv.reader(file)

                print("\nContacts from CSV File:")
                for row in reader:
                    print(", ".join(row))

        except FileNotFoundError:
            print("CSV file not found. No data to read.")
