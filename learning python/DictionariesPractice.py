book = {
    'title' : 'Dune',
    'author' : 'Frank',
    'year' : 1964,
    'genre' : 'scifi'
    }

print(book)
print(book['title'], book['author'])

book['year'] = 1965
book['pages'] = 412

book.pop('genre')

print(book)
