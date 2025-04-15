from graphene_django import DjangoObjectType

from apps.book.models import Book, BookCategory, BookGenre


class BookCategoryType(DjangoObjectType):
    class Meta:
        model = BookCategory
        fields = ('id', 'name')


class BookGenreType(DjangoObjectType):
    class Meta:
        model = BookGenre
        fields = ('id', 'name')


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ('id', 'title', 'summary', 'cover', 'category', 'genres')

