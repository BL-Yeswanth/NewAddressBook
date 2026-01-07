from contact import Contact


class AddressBookMain:
    def start(self):
        print("Welcome to Address Book Program")
        
        # UC1 : Ability to create a contact 
        contact = Contact(
            first_name=input("Enter First Name: "),
            last_name=input("Enter Last Name: "),
            address=input("Enter Address: "),
            city=input("Enter City: "),
            state=input("Enter State: "),
            zip_code=input("Enter Zip Code: "),
            phone_number=input("Enter Phone Number: "),
            email=input("Enter Email: ")
        )

        contact.display()


if __name__ == "__main__":
    app = AddressBookMain()
    app.start()
