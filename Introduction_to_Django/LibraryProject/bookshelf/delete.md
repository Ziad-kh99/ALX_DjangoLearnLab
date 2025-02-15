book = Book.objects.filter(title='Nineteen Eighty-Four').first()
book.delete()
# (1, {'bookshelf.Book': 1})
Book.objects.all()
# <QuerySet []>

