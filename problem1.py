class Book:
    def __init__(self, book_name, book_author, book_type) -> None:
        self.book_name = book_name
        self.book_author = book_author
        self.book_type = book_type


Book1 = Book("Dalalar kitobi", "Tog'ay Murod", "tarixiy kitob")

Book_name = Book1.book_name
Book_author = Book1.book_author
Book_type = Book1.book_type
print(f"Otamdan qolgan {Book_name} muallifi {Book_author}, kitob {Book_type}lar toifasiga kiradi")

Book1.book_name = "O'tgan kunlar"
Book1.book_author = "Abdullar Qodiriy"
Book1.book_name = "Badiy kitob"

print("")
print(f"Otamdan qolgan {Book_name} dan {Book1.book_name}ga o'zgartirildi")

print(f"\n{Book_author} muallifidan {Book1.book_author} muallifiga o'zgartirildi")