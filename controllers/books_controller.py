
from flask import Flask, redirect, render_template, Blueprint, request, redirect
from repositories import book_repository, author_repository
from models.book import Book


books_blueprint = Blueprint('books',__name__)

@books_blueprint.route('/')
def home():
    return render_template('index.html')

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/books.html", all_books=books)

@books_blueprint.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors=authors)

@books_blueprint.route("/books/addbook", methods=['POST'])
def add_book():
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']
    price = request.form['price']
    author_object = author_repository.select(author_id)
    books_to_update = Book(title,genre,price,author_object,id)
    book_repository.save(books_to_update)
    return redirect('/books')

@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')

@books_blueprint.route("/books/<id>", methods=['GET'])
def show_book (id):
    book = book_repository.select(id)
    return render_template('books/show.html', book=book)

@books_blueprint.route('/books/<id>', methods=['POST'])
def update(id):
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']
    price = request.form['price']
    author_object = author_repository.select(author_id)
    books_to_update = Book(title,genre,price,author_object,id)
    book_repository.update(books_to_update)
    return redirect('/books')

@books_blueprint.route('/books/<id>/edit', methods=['GET'])
def edit_book(id):
    book= book_repository.select(id)
    authors_list = author_repository.select_all()
    return render_template('books/edit.html', book = book, all_authors=authors_list)