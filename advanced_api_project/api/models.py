from django.db import models

class Author(models.Model):
    """
    This model represents an author of books.
    """
    name = models.CharField(max_length=100)

class Book(models.Model):
    """
    This model represents a book with its title, publication year, and author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)