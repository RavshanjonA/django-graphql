from django.contrib.postgres.search import SearchVector
from django.shortcuts import get_object_or_404

from apps.book.models import Book, BookCategory, BookGenre


def resolve_books(id=None, ct_id=None, gn_id=None, search=None, ):
    queryset = Book.objects.all()
    if id:
        try:
            queryset = queryset.filter(pk=id)
        except Book.DoesNotExist:
            raise Exception(f"with {id} book doesnot exist")
    if ct_id:
        queryset = queryset.filter(category=ct_id)
    if gn_id:
        queryset = queryset.filter(genres__in=gn_id)
    if search:
        queryset = queryset.annotate(
            search=SearchVector('title', 'summary', 'category__name', 'genres__name')).filter(search=search)
    return queryset


def resolve_category(id):
    return get_object_or_404(BookCategory, id=id)


def resolve_categories():
    return BookCategory.objects.all()


def resolve_genres():
    return BookGenre.objects.all()