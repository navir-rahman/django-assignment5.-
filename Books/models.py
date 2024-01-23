from django.db import models
from Categories.models import Category
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
# Every book has title, description,image, borrowing price, user reviews category


class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    image = models.ImageField(upload_to='book_images/')
    price = models.IntegerField()
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    review = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    available_copies = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.title