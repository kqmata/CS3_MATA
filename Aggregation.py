class Book:
    def __init__(self, title: str):
        self.title = title

    def __del__(self):
        print(f"Book object destroyed: '{self.title}'")

class Library:
    def __init__(self, books: list[Book] = None):
        # The Library accepts already-existing Book objects
        self.books = books if books else []

    def __del__(self):
        print("Library object destroyed.")

# 1. Create books outside first (they exist independently of any Library)
book1 = Book("The Hobbit")
book2 = Book("1984")

# 2. Pass existing book objects into the container class
my_library = Library([book1, book2])
print(f"Library populated with: {[b.title for b in my_library.books]}")

# 3. Destroy the library container
print("\nExecuting: del my_library")
del my_library  # Wipes out the library object container

# 4. Check that the child objects survive
print("\nChecking variable accessibility after container deletion:")
print(f"Still active in memory -> book1: {book1.title}")
print(f"Still active in memory -> book2: {book2.title}")