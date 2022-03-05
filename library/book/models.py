from django.db import models

from author.models import Author

class Book(models.Model):
    name = models.CharField(blank=True, max_length=120)
    description = models.TextField(blank=True)
    count = models.IntegerField(default=10)
    author = models.ManyToManyField(Author, related_name='books')