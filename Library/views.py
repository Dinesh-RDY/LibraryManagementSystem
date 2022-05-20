from django.shortcuts import render
from .models import Books
# Create your views here.
def indexView(req):
    return render(req,"index.html",{'text': "index Page"})

def showBooks(req):
    books = Books.objects.all()
    print(books[0])
    return render(req, "books.html", {"books": books})