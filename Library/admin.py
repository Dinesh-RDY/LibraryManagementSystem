from django.contrib import admin
from .models import Department,Books,LibraryUsers
# Register your models here.

admin.site.register(Department)
admin.site.register(Books)
admin.site.register(LibraryUsers)