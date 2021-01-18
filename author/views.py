from django.shortcuts import render
from .models import Author
from django.core.exceptions import ObjectDoesNotExist


def all_authors(request):
    authors = list(Author.objects.all())
    return render(request, 'author/all_authors.html', {'title': "All authors", "authors": authors})


# Create your views here.

def author_by_id(request, id=0):
    author_by_id = Author.objects.get(id=id)
    return render(request, 'author/author_by_id.html', {'title': "Author by id", "author_by_id": author_by_id})


def author_update(request):
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
    authors = list(Author.objects.all())
    return render(request, 'author/all_authors.html', {'title': "All authors", "authors": authors})


def author_delete(request, id=0):
    author = Author.objects.get(id=id)
    author.delete()
    # Book.save()
    authors = list(Author.objects.all())
    return render(request, 'author/all_authors.html', {'title': "All authors", "authors": authors})
