class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, number):
        contact = Contact(name, number)
        self.contacts.append(contact)

    def remove_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact.number
        return "Contact not found"

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Number: {contact.number}")

# Example usage
phonebook = Phonebook()
phonebook.add_contact("Alice", "1234")
phonebook.add_contact("Bob", "5678")
phonebook.display_contacts()
print(phonebook.search_contact("Alice"))
phonebook.remove_contact("Alice")
phonebook.display_contacts()
