from django.shortcuts import redirect, render
from .models import Books, Department, LibraryUsers
from .forms import DropDownForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from pprint import pprint
# Create your views here.


def indexView(req):
    print("Hello")
    return render(req, "index.html", {'text': "index Page", "user": LibraryUsers})


@login_required
def showBooks(req):
    dept = req.GET.get("menu")
    current_user = LibraryUsers.objects.filter(user=req.user)[0]
    if dept:
        books = Books.objects.filter(dept=dept)
        filter = True
    else:
        books = Books.objects.all()
        filter = False
    return render(req, "books.html", {"books": books,
                                      "dropdown": DropDownForm,
                                      "librarian": current_user.is_librarian,
                                      "filter": filter
                                      })


@login_required
def showDetails(req, pk):
    # book = Books.objects.filter(bookid=pk)[0]
    # user = req.user
    # return render(req, "book_details.html", {"book": book, "user": user})
    with open('static/pdfs/1.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type="application/pdfs")
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response


@login_required
def userLogout(req):
    logout(req)
    return HttpResponseRedirect("/login")


def loginPage(req):
    if req.method == 'POST':
        print("Post")
        username = req.POST.get("username")
        password = req.POST.get("password")
        user = authenticate(req, username=username, password=password)
        if user:
            if user.is_active:
                login(req, user)
                return HttpResponseRedirect("books")
            else:
                return HttpResponse("Account not active")
        else:
            print("Not a user ")
    return render(req, "login.html", {"loginform": UserLoginForm()})
