from publication import Publication

class Borrower:
    MAX_BOOKS = 3

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.__borrowed_books = []      # Encapsulation

    def borrow_book(self, book):
        if len(self.__borrowed_books) >= Borrower.MAX_BOOKS:
            print(f"{self.name} cannot borrow more than {Borrower.MAX_BOOKS} books.")
            return

        if book.is_available():
            self.__borrowed_books.append(book)
            book.set_availability(False)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is currently not available.")

    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.set_availability(True)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    def display_borrowed_books(self):
        print(f"\nBooks borrowed by {self.name}:")

        if not self.__borrowed_books:
            print("No books borrowed.")
        else:
            for book in self.__borrowed_books:
                print(f"- {book.title}")

    def display_member_details(self):
        print(f"""
Member Details
--------------
ID : {self.member_id}
Name : {self.name}
Books Borrowed : {len(self.__borrowed_books)}
""")