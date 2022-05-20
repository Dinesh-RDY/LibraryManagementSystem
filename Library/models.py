from django.db import models

# Create your models here.

class Department(models.Model):
    deptName = models.CharField(max_length=50)
    deptid = models.CharField(primary_key=True, max_length=254)

    def __str__(self) -> str:
        return self.deptName

class Books(models.Model):
    bookid = models.IntegerField(primary_key=True)
    author = models.CharField(max_length= 100)
    publisher = models.CharField(max_length= 100)
    name = models.CharField(max_length= 200)
    pages = models.IntegerField()
    cost = models.IntegerField()
    dept = models.ForeignKey(to="Department",on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

