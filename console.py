from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Robert", "Jordan")
author_repository.save(author1)
author2 = Author("Donald", "Trump")
author_repository.save(author2)

book1 = Book("Lord of Ashes", 'fantasy', 8, author1)
book_repository.save(book1)

book2 = Book("Grab them good", 'biopic', 2, author2)
book_repository.save(book2)

books=book_repository.select_all()
print (books)