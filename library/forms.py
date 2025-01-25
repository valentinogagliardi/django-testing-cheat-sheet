from django import forms
from library.models import Book


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)

    class Meta:
        model = Book
        fields = ["title", "authors"]

        labels = {
            "title": "Insert the book title",
            "authors": "Select the book authors",
        }
