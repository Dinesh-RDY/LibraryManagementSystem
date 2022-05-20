from django.urls import path
from .views import indexView,showBooks
app_name = "Library"
urlpatterns = [
    path("", indexView , name="IndexView"),
    path("books/", showBooks, name= "showBooks")
]