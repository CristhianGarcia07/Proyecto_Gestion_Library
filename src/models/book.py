class Book:
    def __init__(self, book_id, title, author, year, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        estado = "Disponible" if self.available else "Prestado"
        return f"{self.book_id} - {self.title} ({self.author}, {self.year}) [{estado}]"
    
# prueba de cambio1
# prueba de cambio2