#Q8 - CRUD

In this execrise, you are going to create a book library, using CSV files. 

##Create the data access layer

Perform the following tasks:

1. Inside the `data.py` file, finish the function `read_books` that will open the `books.csv` file for reading and read in all the books
into a dictionary named `library`. The key should be `title` and the value a dictionary of all the properties of the book.

2. Finish the `list_book` function, which will go through the `library` dictionary and extract each book's title into a list. Return the list from the function

3. Finish the `find_book` function, which takes in one argument which is the title of a book, and uses the `library` dictionary to find a book with that title. 
The function will return the dictionary that represents the book.

4. Finish the `add_book` function, which takes in a title, ISBN, author and year published. Add the new book as a row inside the `books.csv` file.
Ensure that the ISBN is unique.

5. Finish the `modify_book` function, which takes in the ISBN of a book, and has the following arguments: title, year published and author. Replace the book 
in the `library` dictionary with the title, year published and author that are passed in.

6. Finish the `delete_book` function, which takes in the ISBN of a book. Remove the book from the `library` dictionary with that ISBN.

7. Finish the `save` function, which will save the content of the `library` dictionary into the `books.csv` file, overwriting the file's old content.

8. Make sure all test cases for `data.py` passed. To do so, in the terminal, type in:

`py.test data_tests.py`

## Coding the interface
Create a new Flask app inside `app.py` (important: for the automated marking to work, it must be `app.py`)

Add in the following routes:

### /
Display all the books in the system using in an unodered list (using `<ul>`), with the book title in each list item (`<li></li>`)

### GET /search
Create a form that allows the user to search for a book by title. 

### POST /search
Display books that match the user's query that they entered in `POST /search`

### GET /add
Displays the form that allows the user to add in a book.

### POST /add
Process the form that allows the user to add in a book (from `GET /add`). Before adding, make sure the book's ISBN is unique

### GET /edit/<ISBN>
Display a form which allows the user to modify the details of a book specified by the ISBN

### POST /edit/<ISBN>
Modify the details of a book specified by the ISBN

### GET /choose_delete
Display a list of books. Allow the user to select one to delete.

### GET /delete_book/<ISBN>
Confirm with the user if they wish to delete a book specified by the ISBN 

### POST /delete_book/<ISBN>
Delete the book specified by the ISBN