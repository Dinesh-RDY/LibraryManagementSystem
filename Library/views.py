from django.shortcuts import redirect, render
from .models import Books
from .forms import DropDownForm
# Create your views here.
def indexView(req):
    return render(req,"index.html",{'text': "index Page"})

def showBooks(req):
    if req.method == "POST":
        print("Post")
        
    books = Books.objects.all()
    return render(req, "books.html", {"books": books ,"dropdown":DropDownForm})