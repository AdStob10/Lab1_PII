from library import Library

if __name__ == '__main__':
    library = Library({"99779342526": "Test book"})
    book = library.find_book("99779342526")
    if book is not None:
        print(book)