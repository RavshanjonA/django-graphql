from django.contrib import admin

from book.models import Book, BookCategory, BookGenre

admin.site.register([Book, BookCategory, BookGenre])
