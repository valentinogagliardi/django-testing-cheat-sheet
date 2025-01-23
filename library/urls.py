from django.urls import path, include
from library.views import BookDetailView

urlpatterns = [
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
]
