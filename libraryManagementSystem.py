class Book:
    def __init__(self, book_id, title, author, year, status):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.next = None

class Library:
    def __init__(self):
        self.head = None

    def add_book(self, book_id, title, author, year, status):
        new_book = Book(book_id, title, author, year, status)
        if not self.head or self.head.book_id > book_id:
            new_book.next = self.head
            self.head = new_book
        else:
            current = self.head
            while current.next and current.next.book_id < book_id:
                current = current.next
            new_book.next = current.next
            current.next = new_book
        print(f"Book '{title}' added.")

    def remove_book(self, book_id):
        current = self.head
        previous = None
        while current and current.book_id != book_id:
            previous = current
            current = current.next
        if not current:
            print(f"Book with ID {book_id} not found.")
            return
        if not previous:
            self.head = current.next
        else:
            previous.next = current.next
        print(f"Book with ID {book_id} removed.")

    def search_book(self, attribute, value):
        current = self.head
        results = []
        while current:
            if ((attribute == 'book_id' and current.book_id == value) or
                (attribute == 'title' and current.title == value) or
                (attribute == 'author' and current.author == value)):
                results.append(current)
            current = current.next
        return results

    def display_books(self):
        current = self.head
        if not current:
            print("Library is empty.")
            return
        while current:
            print(f"ID: {current.book_id}, Title: {current.title}, Author: {current.author}, Year: {current.year}, Status: {current.status}")
            current = current.next

def library_system():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            book_id = int(input("Enter book ID: "))
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")
            status = input("Enter status: ")
            library.add_book(book_id, title, author, year, status)
        elif choice == "2":
            book_id = int(input("Enter book ID to remove: "))
            library.remove_book(book_id)
        elif choice == "3":
            attribute = input("Search by (book_id, title, author): ")
            value = input("Enter search value: ")
            results = library.search_book(attribute, value)
            if results:
                for book in results:
                    print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
            else:
                print("No matching books found.")
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")

# Run the library system
library_system()
