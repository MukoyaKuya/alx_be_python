# main.py
from book_class import Book

def main():
    # Create a Book instance
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating __str__
    print(my_book)  # Expected: 1984 by George Orwell, published in 1949

    # Demonstrating __repr__
    print(repr(my_book))  # Expected: Book('1984', 'George Orwell', 1949)

    # Delete the book to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
