class Author:
    
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
        self.contract = []

    def contracts(self):
        return [contracts for contracts in Contract.all]


class Book:
   
    def __init__(self, title):
        if isinstance(title, str):
            self.title = title


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
            if not isinstance(author, Author):
                raise TypeError('author is not an instance of Author')
            if not isinstance(book, Book):
                raise TypeError('book is not an instance of Book')
            if not isinstance(date, str):
                raise TypeError('date is should be a string')
            if not isinstance(royalties, int):
                raise TypeError('royalties should be a number')
            
            self.author = author
            self.book = book
            self.date = date
            self.royalties = royalties
            Contract.all.append(self)

            
