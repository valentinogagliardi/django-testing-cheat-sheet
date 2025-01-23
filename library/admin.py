from django.contrib import admin
from library.models import Book, Author

admin.site.register([Book, Author])
