class Book:
    def __init__(self, title,) -> None:
        self.title = title

class Library:
    def __init__(self) -> None:
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def showBooks(self):
        for book in self.books:
            print(f" Title: {book.title}")
    
b1 = Book("Arabi")
l = Library()
l.add_books(b1)
b2 = Book("pyhsics")
l = Library()
l.add_books(b2)
b3 = Book("Python")
l = Library()
l.add_books(b3)
b4 = Book("Math")
l = Library()
l.add_books(b4)
b5 = Book("Islamiat")
l = Library()
l.add_books(b5)
b6 = Book("Urdu")
l = Library()
l.add_books(b6)
b7 = Book("Chemistry")
l = Library()
l.add_books(b7)
b8 = Book("English")
l = Library()
l.add_books(b8)
b9 = Book("PST")
l = Library()
l.add_books(b9)
b10 = Book("Java")
l.showBooks()




class Department:
    def __init__(self, name) -> None:
        self.name = name

class University:
    def __init__(self, name) -> None:
        self.name = name
        self.departments =[]

    def add_department(self,department):
        self.departments.append(department)

dept1 = Department("Computer Science") 
dept2 = Department("Electrical Engineering")

university = University("ABC University")
university.add_department(dept1)
university.add_department(dept2)
print(dept1)
print(dept2)