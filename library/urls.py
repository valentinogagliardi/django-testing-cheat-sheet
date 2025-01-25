from django.urls import path
from library.views import BookDetailView, BookCreateView

urlpatterns = [
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("books/create/", BookCreateView.as_view(), name="book_create"),
]
