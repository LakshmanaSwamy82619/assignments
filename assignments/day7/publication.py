class Publication:
    def __init__(self, title, author, isbn):
        # Store basic information about the publication (like a book)
        self.title = title
        self.author = author
        self.isbn = isbn

        # __available is private (Encapsulation)
        # Name starts with double underscore, so Python will internally convert it to:
        # self._Publication__available
        self.__available = True

    # Getter method: This lets other code safely check if the book is available
    def is_available(self):
        # Return the private availability flag
        return self.__available

    # Setter method: This lets other code update availability in a controlled way
    def set_availability(self, status):
        # Update the private flag
        self.__available = status

    def display_details(self):
        # Convert boolean availability into a user-friendly message
        status = "Available" if self.__available else "Borrowed"

        # Print details in a clean formatted block
        print(
            f"""
Book Details
------------
Title  : {self.title}
Author : {self.author}
ISBN   : {self.isbn}
Status : {status}
""")
