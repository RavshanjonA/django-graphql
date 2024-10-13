from dataclasses import field
from html.parser import interesting_normal
from ipaddress import summarize_address_range
from re import search

import graphene
from django.contrib.postgres.search import SearchVector
from django.shortcuts import get_object_or_404
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload

from .models import Book, BookCategory, BookGenre


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
        fields = ('id', 'title', 'summary', 'file', 'category', 'genres')


class Query(graphene.ObjectType):
    books = graphene.List(BookType, id=graphene.Int(), ct_id=graphene.Int(), gn_id=graphene.List(graphene.Int),
                          search=graphene.String())
    categories = graphene.List(BookCategoryType, id=graphene.Int())
    category = graphene.Field(BookCategoryType, id=graphene.Int())

    def resolve_category(self, info, id):
        category = get_object_or_404(BookCategory, pk=id)
        return category

    def resolve_books(self, info, id=None, ct_id=None, gn_id=None, search=None, **kwargs):
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

    def resolve_categories(self, info,**kwargs):
        queryset = BookCategory.objects.all()
        return queryset


class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        summary = graphene.String(required=True)
        # file = Upload(required=True)
        category = graphene.Int(required=True)
        genres = graphene.List(graphene.ID, required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, title, summary, category, genres):
        category = BookCategory.objects.get(id=category)
        genres = BookGenre.objects.filter(id__in=genres)
        book = Book(
            title=title,
            summary=summary,
            # file=file,
            category=category
        )
        book.save()
        book.genres.set(genres)
        return CreateBook(book=book)


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
