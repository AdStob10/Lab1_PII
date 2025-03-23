class Library:
    def __init__(self, books: dict[str, str]):
        self.books = books

    def find_book(self, isbn: str) -> str or None:
        if isbn in self.books:
            return self.books[isbn]
        else:
            return None
