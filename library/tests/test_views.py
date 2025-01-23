from django.test import TestCase, RequestFactory
from library.models import Book, Author

from library.views import BookDetailView


class TestDetail(TestCase):
    def test_detail(self):
        factory = RequestFactory()
        request = factory.get("/books/1/")

        view = BookDetailView.as_view()

        author = Author.objects.create(first_name="Jane", last_name="Doe")
        book = Book.objects.create(title="Test Book")
        book.authors.add(author)

        with self.subTest("Render the full template"):
            request.htmx = False

            response = view(request, pk=book.pk)
            self.assertContains(response, "Test Book")
            self.assertContains(response, "Jane Doe")

        with self.subTest("Render the partial template"):
            request.htmx = True

            response = view(request, pk=book.pk)
            self.assertContains(response, "Test Book")
            self.assertContains(response, "Jane Doe")
