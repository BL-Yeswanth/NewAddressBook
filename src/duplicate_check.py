# UC7: Check duplicate contact by first name

class DuplicateCheck:
    def __init__(self, contacts):
        self.contacts = contacts

    def is_duplicate(self, first_name):
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower():
                return True
        return False
