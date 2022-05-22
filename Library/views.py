from django.shortcuts import redirect, render
from .models import Books, Department
from .forms import DropDownForm
# Create your views here.


def indexView(req):
    return render(req, "index.html", {'text': "index Page"})


def showBooks(req):

    dept = req.GET.get("menu")
    if dept:
        books = Books.objects.filter(dept=dept)
    else:
        books = Books.objects.all()
    return render(req, "books.html", {"books": books, "dropdown": DropDownForm})


def showDetails(req, pk):
    book = Books.objects.filter(bookid=pk)[0]
    print(type(book))
    return render(req, "book_details.html", {"book": book})
