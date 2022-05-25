from django.shortcuts import redirect, render
from .models import Books, Department, LibraryUsers
from .forms import DropDownForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def indexView(req):
    print("Hello")
    return render(req, "index.html", {'text': "index Page", "user": LibraryUsers})


@login_required
def showBooks(req):
    dept = req.GET.get("menu")
    if dept:
        books = Books.objects.filter(dept=dept)
    else:
        books = Books.objects.all()
    return render(req, "books.html", {"books": books, "dropdown": DropDownForm})


@login_required
def showDetails(req, pk):
    book = Books.objects.filter(bookid=pk)[0]
    print(type(book))
    return render(req, "book_details.html", {"book": book})


@login_required
def userLogout(req):
    logout(req)
    return HttpResponseRedirect("/")


def loginPage(req):
    print("LoginPage")
    if req.method == 'POST':
        print("Post")
        username = req.POST.get("username")
        password = req.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                print("In here")
                login(req, user)
                return HttpResponseRedirect("books")
            else:
                return HttpResponse("Account not active")
        else:
            print("Not a user ")
    return render(req, "login.html", {"loginform": UserLoginForm()})
