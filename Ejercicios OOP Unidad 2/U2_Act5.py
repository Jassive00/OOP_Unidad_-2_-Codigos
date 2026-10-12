"""Act 5. Create a class Book wigth attributes title and num_page. Override:
__str__() to print "Book: X, Pages: Y".
__len__() so that len(book) returns the number of pages."""
class Libro: # We create a class called Libro.
    def __init__(self, titulo, num_paginas): # Constructor: accepts the title and the number of page.
        self.titulo = titulo # We store the title in the self.title attribute.
        self.num_paginas = num_paginas # We store the number of pages in the self.num_page attribute

    def __str__(self): # We override the special method __str__().
        return f"Libro: {self.titulo}, Paginas: {self.num_paginas}"
        # This method defines how the object is displayed when we use print().
        # It returns a string containing the title and the number of pages.

    def __len__(self): # We override the special method __len__().
        return self.num_paginas
        # This method defines what happens when we use len() on the object.
        # It returns the number of pages in the book.
"""In this section, the Book class is defined with two attributes 
(title and num_pages) and two special methods:
__str__() controls how the object is printed.
__len__() allows you to use len() to get the number of pages."""

libro1 = Libro("Cien años de soledad", 471) # We create an object of the Book class with a title and pages.
print(libro1) # When the object is printed, __str__() is automatically called.
print("Número de páginas:", len(libro1)) # When you use len(), __len__() is called and returns the number of pages.
"""When you use len(libro1), Python calls the __len__() method and returns 471."""