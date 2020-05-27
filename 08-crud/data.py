import csv

# Inside the data.py file, finish the function read_books that will open the books.csv file for reading and read in all the books into a dictionary named library. The key should be title and the value a dictionary of all the properties of the book.


def read_books():
    library = []
    with open('books.csv', 'r', newline='\n') as books:
        reader = csv.reader(books, delimiter=",")
        next(reader)
        for line in reader:
            library.append({
                'ISBN': line[0],
                'title': line[1],
                'author': line[2]
            })
    return library

# Finish the list_book function, which will go through the library dictionary and extract each book's title into a list. Return the list from the function


def list_book(library):
    list_of_books = []
    for book in library:
        for k, v in book.items():
            if k == 'title':
                list_of_books.append(v)
    return list_of_books


# Finish the find_book function, which takes in one argument which is the title of a book, and uses the library dictionary to find a book with that title. The function will return the dictionary that represents the book.

def find_book(title):
    library = read_books()
    books = []
    for b in library:
        if b['title'] == title:
            books.append(b)
    return books

# Finish the add_book function, which takes in a title, ISBN, author and year published. Add the new book as a row inside the books.csv file. Ensure that the ISBN is unique.

def add_book(book):
   pass

