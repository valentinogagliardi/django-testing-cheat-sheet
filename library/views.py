from django.views.generic import DetailView
from library.models import Book


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"

    def get(self, request, *args, **kwargs):
        if request.htmx:
            self.template_name = "library/partials/book.html"
        return super().get(request, *args, **kwargs)
