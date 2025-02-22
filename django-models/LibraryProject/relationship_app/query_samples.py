from .models import Book, Author, Library, Librarian



#> Query all books by a specific author:
author_name = input('Enter author name: ')
author = Author.objects.get(name=author_name)

if author:
    books = Book.objects.filter(author=author)
else:
    print('No author found with that name.')




#> List all books in a library:
library_name = input('Enter Library Name: ')
library = Library.objects.get(name=library_name)

if library:
    books = library.books.all()



#> Retrieve the librarian for a library:
library_name = input('Enter Library Name: ')
library_name = Library.objects.get(name=library_name)

if library:
    librarian = Librarian.objects.filter(library=library_name)

