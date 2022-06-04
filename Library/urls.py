from django.urls import path
from .views import indexView, showBooks, showDetails, userLogout, loginPage
app_name = "Library"
urlpatterns = [
    path("", indexView, name="IndexView"),
    path("books/", showBooks, name="showBooks"),
    path("bookDetails/<int:pk>", showDetails, name="detailsPage"),
    path("logout", userLogout, name="logout"),
    path("login" , loginPage, name="loginPage"),
]
