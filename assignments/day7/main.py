from publication import Publication
from borrower import Borrower

book1 = Publication("Python Basics", "Alice", "ISBN001")
book2 = Publication("Learning OOP", "Bob", "ISBN002")
book3 = Publication("Data Structures", "Charlie", "ISBN003")
book4 = Publication("Algorithms", "David", "ISBN004")

member1 = Borrower(101, "John")
member2 = Borrower(102, "Emma")

member1.borrow_book(book1)
member1.borrow_book(book2)
member1.borrow_book(book3)

# John tries to borrow a fourth book.
# The system should not allow more than 3 books.
member1.borrow_book(book4)

# Emma tries to borrow Book 1.
# Since John already borrowed it,
# the system should display a message.
member2.borrow_book(book1)

member1.display_member_details()
member1.display_borrowed_books()

print("\nLibrary Books:")

book1.display_details()
book2.display_details()
book3.display_details()
book4.display_details()

# John returns Book 1
member1.return_book(book1)
print("\nAfter Returning:")

# Display Book 1 details after returning
book1.display_details()