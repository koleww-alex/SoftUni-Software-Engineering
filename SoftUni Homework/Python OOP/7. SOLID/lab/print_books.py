class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class Printer(Formatter):
    def get_book(self, book: Book):
        formatted_book = self.format(book)
        return formatted_book


book = Book('az sum Sasho')

p = Printer()
print(p.get_book(book))
