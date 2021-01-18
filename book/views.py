from django.shortcuts import render
from .models import Book, Author
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import admin


def all_books(request):
    books = list(Book.objects.all())
    return render(request, 'book/all_books.html', {'title': "All books", "books": books})


def ad(request):
    return render(request, admin.site.urls)


def all_books_by_name(request):
    books = list(Book.objects.all())

    return render(request, 'book/all_books_by_name.html', {'title': "All books by name", "books": books})


def book_by_id(request, id=0):
    book_by_id = Book.objects.get(id=id)
    return render(request, 'book/book_by_id.html', {'title': "Book by id", "book_by_id": book_by_id})


def test(request):
    books = list(Book.objects.all())
    return render(request, 'book/book_plus.html', {'title': "All books", "books": books})


def book_update(request):
    # def book_update(request, book_id=0, name, description, author, count):
    # if name:
    #     Book.objects.get(id=book_id).name = name
    # if description:
    #     Book.objects.get(id=book_id).description = description
    # if author:
    #     Book.objects.get(id=book_id).author = author
    # if count:
    #     Book.objects.get(id=book_id).count = count
    # Book.save()
    books = list(Book.objects.all())
    return render(request, 'book/all_books.html', {'title': "All books", "books": books})


def book_delete(request, id=0):
    book = Book.objects.get(id=id)
    book.delete()
    # Book.save()
    books = list(Book.objects.all())
    return render(request, 'book/all_books.html', {'title': "All books", "books": books})
