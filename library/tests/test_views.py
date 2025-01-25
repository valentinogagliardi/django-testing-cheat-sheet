from django.test import TestCase, RequestFactory
from bs4 import BeautifulSoup

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


class TestBookCreateView(TestCase):
    def test_form_labels(self):
        response = self.client.get("/books/create/")
        soup = BeautifulSoup(response.content, "html.parser")

        expected_labels = [
            "Insert the book title",
            "Select the book authors",
        ]

        for label in expected_labels:
            label_el = soup.find("label", text=label)
            self.assertIsNotNone(
                label_el,
                f"Label {label} not found",
            )
            self.assertIsNotNone(
                soup.find(attrs={"id": label_el.get("for")}),
                f"Element with {label} not found",
            )
