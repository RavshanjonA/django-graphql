from django.contrib import admin

from apps.book.models import Book, BookCategory, BookGenre

admin.site.register([Book, BookCategory, BookGenre])
