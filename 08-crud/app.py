from flask import Flask, render_template, request, redirect, url_for
import os
import csv
import random

app = Flask(__name__)


@app.route('/')
def show_books():
    library = read_books()
    return render_template('show_books.template.html', books=library)


@app.route('/search')
def search_books():
    return render_template('find_book.template.html')


@app.route('/search', methods=['POST'])
def search_results():
    title = request.form.get('title')
    matches = find_book(title)
    return render_template('show_books.template.html', books=matches)

# Displays the form that allows the user to add in a book.
@app.route('/add')
def add_book():
    return render_template('add_book.template.html')

# Process the form that allows the user to add in a book (from GET /add). Before adding, make sure the book's ISBN is unique
@app.route('/add', methods=['POST'])
def process_add_book():
    with open('books.csv', 'a', newline="\n") as fp:
        writer = csv.writer(fp, delimiter=",")
        isbn = request.form.get('isbn')
        title = request.form.get('title')
        author = request.form.get('author')
        writer.writerow([isbn, title, author])
    return redirect(url_for('show_books'))


@app.route('/edit/<isbn>')
def edit_book(isbn):
    book = find_book_with_isbn(isbn)
    return render_template('edit_book.template.html', book=book)


@app.route('/edit/<isbn>', methods=['POST'])
def process_edit_book(isbn):
    all_books = read_books()
    book_to_edit = find_book_with_isbn(isbn)
    for i in range(len(all_books)):
        if all_books[i]['isbn'] == book_to_edit['isbn']:
            book_to_edit['isbn'] = request.form.get('isbn')
            book_to_edit['title'] = request.form.get('title')
            book_to_edit['author'] = request.form.get('author')
            all_books[i] = book_to_edit
    rewrite_book(all_books)
    return redirect(url_for('show_books'))


@app.route('/delete_book/<isbn>')
def confirm_delete(isbn):
    book = find_book_with_isbn(isbn)
    return render_template('confirm_delete.template.html', book=book)

@app.route('/delete_book/<isbn>', methods=['POST'])
def delete_book(isbn):
    all_books = read_books()
    book_to_delete = find_book_with_isbn(isbn)
    for i in range(len(all_books)):
        if all_books[i]['isbn'] == book_to_delete['isbn']:
            del all_books[i]
            break
    rewrite_book(all_books)
    return redirect(url_for('show_books'))



def read_books():
    library = []
    with open('books.csv', 'r', newline='\n') as books:
        reader = csv.reader(books, delimiter=",")
        next(reader)
        for line in reader:
            library.append({
                'isbn': line[0],
                'title': line[1],
                'author': line[2]
            })
    return library


def list_book(library):
    list_of_books = []
    for book in library:
        for k, v in book.items():
            if k == 'title':
                list_of_books.append(v)
    return list_of_books


def find_book(title):
    library = read_books()
    books = []
    for b in library:
        if title in b['title'].lower():
            books.append(b)
    return books


def find_book_with_isbn(isbn):
    library = read_books()
    book = {}
    for b in library:
        if isbn == b['isbn']:
            book = b
    return book


def rewrite_book(all_books):
    with open('books.csv', 'w', newline="\n") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(['isbn', 'title', 'author'])
        for b in all_books:
            writer.writerow([b['isbn'], b['title'], b['author']])


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
