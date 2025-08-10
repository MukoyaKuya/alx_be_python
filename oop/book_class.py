# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
      
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
              return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation used for debugging and recreating the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
