from django.views.generic import DetailView, CreateView
from library.models import Book
from library.forms import BookForm


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"

    def get(self, request, *args, **kwargs):
        if request.htmx:
            self.template_name = "library/partials/book.html"
        return super().get(request, *args, **kwargs)


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = "/"
