from django.db import models
from django.utils import timezone

class Book(models.Model):

    title = models.CharField(max_length=200)

    author = models.CharField(max_length=100)

    isbn = models.CharField(max_length=20)

    category = models.CharField(max_length=100)

    quantity = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Student(models.Model):

    name = models.CharField(max_length=100)

    roll_no = models.CharField(max_length=20, unique=True)

    department = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class IssueBook(models.Model):


    STATUS_CHOICES = [
        ('Issued', 'Issued'),
        ('Returned', 'Returned'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    return_date = models.DateField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Issued'
    )

    def __str__(self):
        return f"{self.student} - {self.book}"


