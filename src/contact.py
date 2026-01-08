
#  UC1 : Ability to create a contact
class Contact:
    def __init__(self, first_name, last_name, address, city,
                 state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email
    
    def display(self):
        print(
            f"Name   : {self.first_name} {self.last_name}\n"
            f"Addr   : {self.address}, {self.city}, {self.state} - {self.zip_code}\n"
            f"Phone  : {self.phone_number}\n"
            f"Email  : {self.email}\n"
            f"{'-'*30}"
        )

    def __str__(self):
        return (
            f"Name: {self.first_name} {self.last_name}, "
            f"City: {self.city}, State: {self.state}, "
            f"Zip: {self.zip_code}, "
            f"Phone: {self.phone_number}, "
            f"Email: {self.email}"
        )
