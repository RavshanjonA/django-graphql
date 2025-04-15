import graphene
import graphql_jwt
from django.shortcuts import get_object_or_404
from graphene_django.rest_framework import mutation
from graphene_file_upload.scalars import Upload

from apps.book.graphql.serializers import BookSerializer
from apps.book.models import BookCategory, BookGenre, Book
from apps.book.graphql.type import BookType


class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        summary = graphene.String(required=True)
        cover = Upload(required=True)
        category = graphene.Int(required=True)
        genres = graphene.List(graphene.ID, required=True)

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, info, title, summary, category, genres, cover):
        category = BookCategory.objects.get(id=category)
        genres = BookGenre.objects.filter(id__in=genres)
        book = Book(
            title=title,
            summary=summary,
            cover=cover,
            category=category
        )
        book.save()
        book.genres.set(genres)
        return CreateBook(book=book)


class CreateBookSerializer(mutation.SerializerMutation):
    class Meta:
        serializer_class = BookSerializer


class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        summary = graphene.String()
        category = graphene.Int()
        cover = Upload()
        genres = graphene.List(graphene.ID)

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, info, id, **kwargs):
        book = Book.objects.get(id=id)
        genres = kwargs.pop("genres", None)
        for key, value in kwargs.items():
            setattr(book, key, value)
        if genres:
            book.genres.set(genres)
        book.save()
        return UpdateBook(book=book)


class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, info, id):
        book = get_object_or_404(Book, id=id)
        book.delete()
        return DeleteBook(success=True)


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    creates_book = CreateBookSerializer.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
