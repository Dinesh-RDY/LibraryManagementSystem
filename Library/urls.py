from django.urls import path
from .views import indexView, showBooks, showDetails
app_name = "Library"
urlpatterns = [
    path("", indexView, name="IndexView"),
    path("books/", showBooks, name="showBooks"),
    path("bookDetails/<int:pk>", showDetails, name="detailsPage")
]
