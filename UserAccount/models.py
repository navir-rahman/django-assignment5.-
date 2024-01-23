from django.db import models
from Books.models import Book
from django.contrib.auth.models import User

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name="acc")
    borrowed_books = models.ManyToManyField(Book, blank=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
