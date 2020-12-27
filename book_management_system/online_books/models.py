from django.db import models

class Genre(models.Model):
    genre_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.genre_name 

class Author(models.Model):
    author_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.author_name

class Book(models.Model):
    book_title = models.CharField(max_length=100)
    author_fk = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=True)
    genres = models.ManyToManyField('Genre')
    description = models.TextField(max_length=400, null=True, blank=True)
    price = models.FloatField(help_text="In rupees (₹)", null=True, blank=True)

    def __str__(self):
        return self.book_title

