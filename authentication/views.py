from django.shortcuts import render
from .models import CustomUser
from django.core.exceptions import ObjectDoesNotExist


def all_users(request):
    users = list(CustomUser.objects.all())
    return render(request, 'user/all_users.html', {'title': "All users", "users": users})


# Create your views here.

def user_by_id(request, id=0):
    user_by_id = CustomUser.objects.get(id=id)
    return render(request, 'user/user_by_id.html', {'title': "User by id", "user_by_id": user_by_id})


def user_update(request):
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
    users = list(CustomUser.objects.all())
    return render(request, 'user/all_users.html', {'title': "All users", "users": users})


def user_delete(request, id=0):
    user = CustomUser.objects.get(id=id)
    user.delete()
    users = list(CustomUser.objects.all())
    return render(request, 'user/all_users.html', {'title': "All users", "users": users})

