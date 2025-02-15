book = Book.objects.filter(title='1984').first()
book.title
# '1984'
book.author
# 'George Orwell'
book.publication_year
# 1949

