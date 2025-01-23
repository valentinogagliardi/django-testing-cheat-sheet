from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(to=Author)

    def __str__(self):
        return self.title
