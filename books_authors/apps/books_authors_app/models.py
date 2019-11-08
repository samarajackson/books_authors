from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=45)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #authors
    def __repr__(self):
        return f"Book:{self.title}"


class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField()

    def __repr__(self):
        return (f"{self.first_name} {self.last_name}")
        #Wrote:{",".join(self.books.all().values_list('title', flat=True))}
